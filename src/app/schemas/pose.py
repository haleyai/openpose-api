from enum import Enum
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field


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
    """
    Relative point in an image
    """
    x: float = Field(
        title="Relative X-Coordinate",
        description="Represented as a float in the range [0.0,1.0], "
                    "where 0.0 means the extreme left edge of the image"
                    "and 1.0 means the extreme right edge of the image"
    )
    y: float = Field(
        title="Relative Y-Coordinate",
        description="Represented as a float in the range [0.0,1.0], "
                    "where 0.0 means the extreme top edge of the image"
                    "and 1.0 means the extreme bottom edge of the image"
    )
    confidence: float = Field(
        title="confidence in the point accuracy",
        description="Represented as a float in the range [0.0,1.0], "
                    "where 0.0 means completely uncertain"
                    "and 1.0 means complete confidence / 'certainty'"
    )


class Keypoint(Point):
    id: KPId


class Pose(BaseModel):
    """
    Detected location (relative image coordinates) of 25 main body joints / key-points.
    """
    nose: Optional[Point] = Field(title="Location of the Nose")
    neck: Optional[Point] = Field(title="Location of the Neck")
    right_shoulder: Optional[Point] = Field(title="Location of the Right Shoulder")
    right_elbow: Optional[Point] = Field(title="Location of the Right Elbow")
    right_wrist: Optional[Point] = Field(title="Location of the Right Wrist")
    left_shoulder: Optional[Point] = Field(title="Location of the Left Shoulder")
    left_elbow: Optional[Point] = Field(title="Location of the Left Elbow")
    left_wrist: Optional[Point] = Field(title="Location of the Left Wrist")
    mid_hip: Optional[Point] = Field(title="Location of the Groin")
    right_hip: Optional[Point] = Field(title="Location of the Right Hip")
    right_knee: Optional[Point] = Field(title="Location of the Right Knee")
    right_ankle: Optional[Point] = Field(title="Location of the Right Ankle")
    left_hip: Optional[Point] = Field(title="Location of the Left Hip")
    left_knee: Optional[Point] = Field(title="Location of the Left Knee")
    left_ankle: Optional[Point] = Field(title="Location of the Left Ankle")
    right_eye: Optional[Point] = Field(title="Location of the Right Eye")
    left_eye: Optional[Point] = Field(title="Location of the Left Eye")
    right_ear: Optional[Point] = Field(title="Location of the right Ear")
    left_ear: Optional[Point] = Field(title="Location of the Left Ear")
    left_bigtoe: Optional[Point] = Field(title="Location of the Left Big-toe")
    left_smalltoe: Optional[Point] = Field(title="Location of the Left Small-toe")
    left_heel: Optional[Point] = Field(title="Location of the Left Heel")
    right_bigtoe: Optional[Point] = Field(title="Location of the Right Big-toe")
    right_smalltoe: Optional[Point] = Field(title="Location of the Right small-toe")
    right_heel: Optional[Point] = Field(title="Location of the Right Heel")

    @staticmethod
    def from_keypoints(keypoints: List[Keypoint]) -> 'Pose':
        points = dict([(kpt.id, kpt) for kpt in keypoints])
        return Pose(**points)

    def get_keypoint(self, kpid:KPId) -> Keypoint:
        return self.__getattribute__(kpid)


class Person(BaseModel):
    """
    Representation of a detected person, including:

    - estimated age (disabled)
    - estimated gender (disabled)
    - pose
    """
    gender: Optional[float] = Field(
        title="Estimated gender, if enabled.",
        description="Represented as a float in the range [-1.0,1.0], "
                    "where -1.0 means confidently male"
                    "and 1.0 means confidently female"
                    "and numbers close to 0.0 means uncertain"
    )
    age: Optional[int] = Field(title="Estimated age, if enabled")
    pose: Optional[Pose] = Field(title="detected pose key-points")


class Scene(BaseModel):
    """
    Representation of features of and in an image / scene, including:

    - detected people
    - detected vehicles (disabled)
    - detected 'things' (disabled)
    """
    people: List[Person] = Field(
        default_factory=lambda: [],
        title="List of Persons",
        description="List of detected People, in the form of Person objects.",
    )
    vehicles: List[Any] = Field(
        default_factory=lambda: [],
        title="List of Vehicles",
        description="(Disabled) List of detected Vehicles, in the form of Vehicle objects.",
    )
    things: List[Any] = Field(
        default_factory=lambda: [],
        title="List of Things",
        description="(Disabled) List of detected Things, in the form of Thing objects.",
    )


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
