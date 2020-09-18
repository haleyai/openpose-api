import cv2
from functools import lru_cache
import numpy as np
from typing import List
from urllib.request import urlopen
from app.cv.openpose import get_openpose_engine
from app.schemas.pose import Pose, Keypoint, keypoints_info
from app.cv.engine import Engine

BLACK = (0, 0, 0)
GREY = (127, 127, 127)
WHITE = (255, 200, 200)
BLUE = (255, 0, 0)
GREEN = (0, 180, 0)
RED = (0, 0, 200)


font = cv2.FONT_HERSHEY_PLAIN
fontScale = 1
default_colour = (0, 0, 0)
thickness = 1
colours = [WHITE, RED, GREEN]


def pixel(keypoint: Keypoint, width:int, height:int):
    if keypoint is None:
        return 0, 0
    x = 0 if keypoint.x is None or np.isnan(keypoint.x) else int(keypoint.x * width)
    y = 0 if keypoint.y is None or np.isnan(keypoint.y) else int(keypoint.y * height)
    return x, y


def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


def draw_poses(image, poses: List[Pose]):

    height, width, _ = np.shape(image)

    for pose in poses:
        for kpid, kpinfo in keypoints_info.items():

            kp: Keypoint = pose.get_keypoint(kpid)

            if kp is None:
                continue

            colour = colours[kpinfo.side]
            kpt_thickness = 1  # int(kp.confidence * 3)
            kpt_size = int(kp.confidence * 3)

            # Draw keypoint
            kppxl = pixel(kp, width=width, height=height)
            image = cv2.circle(image, kppxl, kpt_size, colour, kpt_thickness)
            # Write Confidence
#            image = cv2.putText(image, f"{kp.confidence:.3f}", kppxl, font, fontScale, colour, 1, cv2.LINE_AA)

            for neighbor_id in kpinfo.connects:
                neighbor = pose.get_keypoint(neighbor_id)
                if neighbor is not None and neighbor.confidence > kp.confidence:
                    # Set the line colour to match the points if they agree, neutral otherwise,
                    if kpinfo.side == keypoints_info[neighbor_id].side:
                        colour = colours[kpinfo.side]
                    else:
                        colour = colours[0]  # "MID" colour

                    # Draw the line
                    image = cv2.line(image, kppxl, pixel(neighbor, width=width, height=height), colour, thickness)


def infer_url(engine: Engine, url):
    print(f"inferring from url:{url}")
    image = url_to_image(url)
    return engine.infer_image(image)


def draw_url(engine: Engine, url):
    image = url_to_image(url)
    poses = engine.infer_image(image)

    draw_poses(image, poses)

    res, out_image = cv2.imencode(".jpg", image)
    return out_image.tostring()


@lru_cache
def get_engine() -> Engine:
    return get_openpose_engine()
