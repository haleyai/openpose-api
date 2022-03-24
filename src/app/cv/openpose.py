from functools import lru_cache
from app.schemas.pose import KPId, Keypoint, Pose
from typing import List
from app.cv.engine import Engine
import numpy as np
import pyopenpose as op

openpose_keypoints = [
    KPId.nose,
    KPId.neck,
    KPId.right_shoulder,
    KPId.right_elbow,
    KPId.right_wrist,
    KPId.left_shoulder,
    KPId.left_elbow,
    KPId.left_wrist,
    KPId.mid_hip,
    KPId.right_hip,
    KPId.right_knee,
    KPId.right_ankle,
    KPId.left_hip,
    KPId.left_knee,
    KPId.left_ankle,
    KPId.right_eye,
    KPId.left_eye,
    KPId.right_ear,
    KPId.left_ear,
    KPId.left_bigtoe,
    KPId.left_smalltoe,
    KPId.left_heel,
    KPId.right_bigtoe,
    KPId.right_smalltoe,
    KPId.right_heel,
]


class OpenPoseEngine(Engine):
    def __init__(self, model_folder="/openpose/models/", **kwargs):
        print("initializing poser")
        params = dict()
        params["model_folder"] = model_folder
        params.update(kwargs)

        self._opWrapper = op.WrapperPython()
        self._opWrapper.configure(params)
        self._opWrapper.start()

    def infer_image(self, image) -> List[Pose]:
        print("inferring from image")
        if image is None:
            print("no image :(")
            return []

        height, width, _ = np.shape(image)

        datum = op.Datum()
        datum.cvInputData = image
        self._opWrapper.emplaceAndPop(op.VectorDatum([datum]))

        raw_keypoints = datum.poseKeypoints

        poses = []
        for person in raw_keypoints:
            person_keypoints = []
            for ix, detected_kpt in enumerate(person):
                if len(detected_kpt) == 3 and detected_kpt[2] > 0.0:
                    person_keypoints.append(
                        Keypoint(
                            id=openpose_keypoints[ix],
                            x=detected_kpt[0] / width,
                            y=detected_kpt[1] / height,
                            confidence=detected_kpt[2],
                        )
                    )
            poses.append(Pose.from_keypoints(keypoints=person_keypoints))

        return poses


engine = OpenPoseEngine()


@lru_cache()
def get_openpose_engine():
    return engine
