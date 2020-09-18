from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel


class Side(int, Enum):
    LEFT = -1
    MID = 0
    RIGHT = 1


class KPId(str, Enum):
    nose = "nose"
    neck = "neck"
    right_shoulder = "right_shoulder"
    right_elbow = "right_elbow"
    right_wrist = "right_wrist"
    left_shoulder = "left_shoulder"
    left_elbow = "left_elbow"
    left_wrist = "left_wrist"
    mid_hip = "mid_hip"
    right_hip = "right_hip"
    right_knee = "right_knee"
    right_ankle = "right_ankle"
    left_hip = "left_hip"
    left_knee = "left_knee"
    left_ankle = "left_ankle"
    right_eye = "right_eye"
    left_eye = "left_eye"
    right_ear = "right_ear"
    left_ear = "left_ear"
    left_bigtoe = "left_bigtoe"
    left_smalltoe = "left_smalltoe"
    left_heel = "left_heel"
    right_bigtoe = "right_bigtoe"
    right_smalltoe = "right_smalltoe"
    right_heel = "right_heel"


class KPMeta(BaseModel):
    description: str
    side: Side
    connects: List[KPId]


class Point(BaseModel):
    x: float
    y: float
    confidence: float


class Keypoint(Point):
    id: KPId


class Pose(BaseModel):
    nose: Optional[Keypoint]
    neck: Optional[Keypoint]
    right_shoulder: Optional[Keypoint]
    right_elbow: Optional[Keypoint]
    right_wrist: Optional[Keypoint]
    left_shoulder: Optional[Keypoint]
    left_elbow: Optional[Keypoint]
    left_wrist: Optional[Keypoint]
    mid_hip: Optional[Keypoint]
    right_hip: Optional[Keypoint]
    right_knee: Optional[Keypoint]
    right_ankle: Optional[Keypoint]
    left_hip: Optional[Keypoint]
    left_knee: Optional[Keypoint]
    left_ankle: Optional[Keypoint]
    right_eye: Optional[Keypoint]
    left_eye: Optional[Keypoint]
    right_ear: Optional[Keypoint]
    left_ear: Optional[Keypoint]
    left_bigtoe: Optional[Keypoint]
    left_smalltoe: Optional[Keypoint]
    left_heel: Optional[Keypoint]
    right_bigtoe: Optional[Keypoint]
    right_smalltoe: Optional[Keypoint]
    right_heel: Optional[Keypoint]

    @staticmethod
    def from_keypoints(keypoints: List[Keypoint]) -> 'Pose':
        points = dict([(kpt.id, kpt) for kpt in keypoints])
        return Pose(**points)

    def get_keypoint(self, kpid:KPId) -> Keypoint:
        return self.__getattribute__(kpid)


keypoints_info: Dict[KPId, KPMeta] = {
    KPId.nose: KPMeta(
        description="Nose", side=Side.MID,
        connects=[KPId.neck, KPId.right_eye, KPId.left_eye, KPId.right_ear, KPId.left_ear]
    ),
    KPId.neck: KPMeta(
        description="Neck", side=Side.MID,
        connects=[KPId.nose, KPId.right_shoulder, KPId.left_shoulder, KPId.mid_hip, KPId.right_hip, KPId.left_hip]
    ),
    KPId.right_shoulder: KPMeta(
        description="RShoulder", side=Side.RIGHT,
        connects=[KPId.neck, KPId.right_elbow, KPId.left_shoulder, KPId.mid_hip, KPId.right_hip, KPId.left_hip]
    ),
    KPId.right_elbow: KPMeta(
        description="RElbow", side=Side.RIGHT,
        connects=[KPId.right_shoulder, KPId.right_wrist]
    ),
    KPId.right_wrist: KPMeta(
        description="RWrist", side=Side.RIGHT,
        connects=[KPId.right_elbow]
    ),
    KPId.left_shoulder: KPMeta(
        description="LShoulder", side=Side.LEFT,
        connects=[KPId.neck, KPId.right_shoulder, KPId.left_elbow, KPId.mid_hip, KPId.right_hip, KPId.left_hip]
    ),
    KPId.left_elbow: KPMeta(
        description="LElbow", side=Side.LEFT,
        connects=[KPId.left_shoulder, KPId.left_wrist]
    ),
    KPId.left_wrist: KPMeta(
        description="LWrist", side=Side.LEFT,
        connects=[KPId.left_elbow]
    ),
    KPId.mid_hip: KPMeta(
        description="MidHip", side=Side.MID,
        connects=[KPId.neck, KPId.right_shoulder, KPId.left_shoulder, KPId.right_hip, KPId.left_hip]
    ),
    KPId.right_hip: KPMeta(
        description="RHip", side=Side.RIGHT,
        connects=[KPId.neck, KPId.right_shoulder, KPId.left_shoulder, KPId.mid_hip, KPId.right_knee, KPId.left_hip]
    ),
    KPId.right_knee: KPMeta(
        description="RKnee", side=Side.RIGHT,
        connects=[KPId.right_hip, KPId.right_ankle]
    ),
    KPId.right_ankle: KPMeta(
        description="RAnkle", side=Side.RIGHT,
        connects=[KPId.right_knee, KPId.right_bigtoe, KPId.right_smalltoe, KPId.right_heel]
    ),
    KPId.left_hip: KPMeta(
        description="LHip", side=Side.LEFT,
        connects=[KPId.neck, KPId.right_shoulder, KPId.left_shoulder, KPId.mid_hip, KPId.right_hip, KPId.left_knee]
    ),
    KPId.left_knee: KPMeta(
        description="LKnee", side=Side.LEFT,
        connects=[KPId.left_hip, KPId.left_ankle]
    ),
    KPId.left_ankle: KPMeta(
        description="LAnkle", side=Side.LEFT,
        connects=[KPId.left_knee, KPId.left_bigtoe, KPId.left_smalltoe, KPId.left_heel]
    ),
    KPId.right_eye: KPMeta(
        description="REye", side=Side.RIGHT,
        connects=[KPId.nose]
    ),
    KPId.left_eye: KPMeta(
        description="LEye", side=Side.LEFT,
        connects=[KPId.nose]
    ),
    KPId.right_ear: KPMeta(
        description="REar", side=Side.RIGHT,
        connects=[KPId.nose]
    ),
    KPId.left_ear: KPMeta(
        description="LEar", side=Side.LEFT,
        connects=[KPId.nose]
    ),
    KPId.left_bigtoe: KPMeta(
        description="LBigToe", side=Side.LEFT,
        connects=[KPId.left_ankle]
    ),
    KPId.left_smalltoe: KPMeta(
        description="LSmallToe", side=Side.LEFT,
        connects=[KPId.left_ankle]
    ),
    KPId.left_heel: KPMeta(
        description="LHeel", side=Side.LEFT,
        connects=[KPId.left_ankle]
    ),
    KPId.right_bigtoe: KPMeta(
        description="RBigToe", side=Side.RIGHT,
        connects=[KPId.right_ankle]
    ),
    KPId.right_smalltoe: KPMeta(
        description="RSmallToe", side=Side.RIGHT,
        connects=[KPId.right_ankle]
    ),
    KPId.right_heel: KPMeta(
        description="RHeel", side=Side.RIGHT,
        connects=[KPId.right_ankle]
    ),
}
