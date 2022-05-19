import cv2
from functools import lru_cache
import numpy as np
import boto3
from typing import List
from urllib.request import urlopen
from app.cv.openpose import get_openpose_engine
from app.schemas.pose import Keypoint, Person
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
thickness = 3
colours = [WHITE, RED, GREEN]

BODY_DRAW_STYLE = {
    'color': RED,
    'thickness': 3,
                  }

HAND_DRAW_STYLE = {
    'color': WHITE,
    'thickness': 1,
}

FACE_DRAW_STYLE = {
    'color': WHITE,
    'thickness': 1,
}

s3 = boto3.resource('s3')


def pixel(keypoint: Keypoint, width: int, height: int):
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


def file_to_image(file):
    contents = file.file.read()
    print(f">> Contents: [{contents[1:5]}...] of length {len(contents)}")
    image = np.fromstring(contents, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


def draw_persons(image, persons: List[Person]):

    height, width, _ = np.shape(image)

    for person in persons:
        for pose, draw_style in zip(
                [person.pose, person.face_pose, person.left_hand_pose, person.right_hand_pose],
                [BODY_DRAW_STYLE, FACE_DRAW_STYLE, HAND_DRAW_STYLE, HAND_DRAW_STYLE]):
            if pose is None:
                continue
            for line in pose._skeleton:
                for kpid1, kpid2 in zip(line[:-1], line[1:]):
                    kp1: Keypoint = pose.get_keypoint(kpid1)
                    kp2: Keypoint = pose.get_keypoint(kpid2)
                    pixel1 = pixel(kp1, width=width, height=height)
                    pixel2 = pixel(kp2, width=width, height=height)
                    if pixel1 == (0, 0) or pixel2 == (0, 0):
                        continue
                    image = cv2.line(
                        image,
                        pixel1,
                        pixel2,
                        draw_style['color'],
                        draw_style['thickness'],
                    )
        bbox_pixels = tuple(np.multiply(np.array(person.bounding_box).reshape((2, 2)), np.array([width, height])).
                            round().astype(int).flatten())
        cv2.rectangle(image,
                      bbox_pixels[0:2],
                      bbox_pixels[2:4],
                      BLACK)  # ,
                      # thickness=1)
    return image


def infer_url(engine: Engine, url):
    print(f"inferring from url:{url}")
    image = url_to_image(url)
    return engine.infer_image(image)


def draw_url(engine: Engine, url):
    image = url_to_image(url)
    persons = engine.infer_image(image)

    draw_persons(image, persons)

    res, out_image = cv2.imencode(".jpg", image)
    return out_image.tostring()


def infer_file(engine: Engine, file):
    print("inferring from file")
    image = file_to_image(file)
    return engine.infer_image(image)


def draw_file(engine: Engine, file):
    image = file_to_image(file)
    persons = engine.infer_image(image)
    draw_persons(image, persons)
    res, out_image = cv2.imencode(".jpg", image)
    return out_image.tostring()


def infer_s3(engine: Engine, bucket, key):
    print(f"inferring from S3 {bucket}:{key}")
    file_stream = s3.Bucket(bucket).Object(key).get()['Body']
    image = cv2.imdecode(np.asarray(bytearray(file_stream.read()), dtype="uint8"),
                         cv2.IMREAD_COLOR)
    image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # im = Image.open(file_stream)
    # return np.array(im)
    return engine.infer_image(image)


def write_text_s3(text, bucket, key):
    print(f"writing to S3 {bucket}:{key}")
    print(text)
    s3_object = s3.Bucket(bucket).Object(key)
    s3_object.put(Body=text)


@lru_cache()
def get_engine() -> Engine:
    return get_openpose_engine()
