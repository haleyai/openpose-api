from enum import Enum
from typing import List, Dict
from pydantic import BaseModel


class ModelEnum(str, Enum):
    openpose = 'openpose'
    posenet = 'posenet'
    coco = 'coco'


class KeypointEnum(str, Enum):
    nose = 'nose'
    neck = 'neck'
    right_shoulder = 'right_shoulder'
    right_elbow = 'right_elbow'
    right_wrist = 'right_wrist'
    left_shoulder = 'left_shoulder'
    left_elbow = 'left_elbow'
    left_wrist = 'left_wrist'
    mid_hip = 'mid_hip'
    right_hip = 'right_hip'
    right_knee = 'right_knee'
    right_ankle = 'right_ankle'
    left_hip = 'left_hip'
    left_knee = 'left_knee'
    left_ankle = 'left_ankle'
    right_eye = 'right_eye'
    left_eye = 'left_eye'
    right_ear = 'right_ear'
    left_ear = 'left_ear'
    left_bigtoe = 'left_bigtoe'
    left_smalltoe = 'left_smalltoe'
    left_heel = 'left_heel'
    right_bigtoe = 'right_bigtoe'
    right_smalltoe = 'right_smalltoe'
    right_heel = 'right_heel'


class Keypoint(BaseModel):
    name: KeypointEnum
    ix: Dict[ModelEnum, int]
    x: float
    y: float


# Shared properties
class Pose(BaseModel):
    keypoints: List[Keypoint]

