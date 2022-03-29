from enum import Enum
from typing import List, Dict, Optional, Any, Tuple
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

    LWristBase = "LWristBase"
    LThumb1CMC = "LThumb1CMC"
    LThumb2Knuckles = "LThumb2Knuckles"
    LThumb3IP = "LThumb3IP"
    LThumb4FingerTip = "LThumb4FingerTip"
    LIndex1Knuckles = "LIndex1Knuckles"
    LIndex2PIP = "LIndex2PIP"
    LIndex3DIP = "LIndex3DIP"
    LIndex4FingerTip = "LIndex4FingerTip"
    LMiddle1Knuckles = "LMiddle1Knuckles"
    LMiddle2PIP = "LMiddle2PIP"
    LMiddle3DIP = "LMiddle3DIP"
    LMiddle4FingerTip = "LMiddle4FingerTip"
    LRing1Knuckles = "LRing1Knuckles"
    LRing2PIP = "LRing2PIP"
    LRing3DIP = "LRing3DIP"
    LRing4FingerTip = "LRing4FingerTip"
    LPinky1Knuckles = "LPinky1Knuckles"
    LPinky2PIP = "LPinky2PIP"
    LPinky3DIP = "LPinky3DIP"
    LPinky4FingerTip = "LPinky4FingerTip"

    RWristBase = "RWristBase"
    RThumb1CMC = "RThumb1CMC"
    RThumb2Knuckles = "RThumb2Knuckles"
    RThumb3IP = "RThumb3IP"
    RThumb4FingerTip = "RThumb4FingerTip"
    RIndex1Knuckles = "RIndex1Knuckles"
    RIndex2PIP = "RIndex2PIP"
    RIndex3DIP = "RIndex3DIP"
    RIndex4FingerTip = "RIndex4FingerTip"
    RMiddle1Knuckles = "RMiddle1Knuckles"
    RMiddle2PIP = "RMiddle2PIP"
    RMiddle3DIP = "RMiddle3DIP"
    RMiddle4FingerTip = "RMiddle4FingerTip"
    RRing1Knuckles = "RRing1Knuckles"
    RRing2PIP = "RRing2PIP"
    RRing3DIP = "RRing3DIP"
    RRing4FingerTip = "RRing4FingerTip"
    RPinky1Knuckles = "RPinky1Knuckles"
    RPinky2PIP = "RPinky2PIP"
    RPinky3DIP = "RPinky3DIP"
    RPinky4FingerTip = "RPinky4FingerTip"

    FaceContour0 = "FaceContour0"
    FaceContour1 = "FaceContour1"
    FaceContour2 = "FaceContour2"
    FaceContour3 = "FaceContour3"
    FaceContour4 = "FaceContour4"
    FaceContour5 = "FaceContour5"
    FaceContour6 = "FaceContour6"
    FaceContour7 = "FaceContour7"
    FaceContour8 = "FaceContour8"
    FaceContour9 = "FaceContour9"
    FaceContour10 = "FaceContour10"
    FaceContour11 = "FaceContour11"
    FaceContour12 = "FaceContour12"
    FaceContour13 = "FaceContour13"
    FaceContour14 = "FaceContour14"
    FaceContour15 = "FaceContour15"
    FaceContour16 = "FaceContour16"
    REyeBrow0 = "REyeBrow0"
    REyeBrow1 = "REyeBrow1"
    REyeBrow2 = "REyeBrow2"
    REyeBrow3 = "REyeBrow3"
    REyeBrow4 = "REyeBrow4"
    LEyeBrow4 = "LEyeBrow4"
    LEyeBrow3 = "LEyeBrow3"
    LEyeBrow2 = "LEyeBrow2"
    LEyeBrow1 = "LEyeBrow1"
    LEyeBrow0 = "LEyeBrow0"
    NoseUpper0 = "NoseUpper0"
    NoseUpper1 = "NoseUpper1"
    NoseUpper2 = "NoseUpper2"
    NoseUpper3 = "NoseUpper3"
    NoseLower0 = "NoseLower0"
    NoseLower1 = "NoseLower1"
    NoseLower2 = "NoseLower2"
    NoseLower3 = "NoseLower3"
    NoseLower4 = "NoseLower4"
    REye0 = "REye0"
    REye1 = "REye1"
    REye2 = "REye2"
    REye3 = "REye3"
    REye4 = "REye4"
    REye5 = "REye5"
    LEye0 = "LEye0"
    LEye1 = "LEye1"
    LEye2 = "LEye2"
    LEye3 = "LEye3"
    LEye4 = "LEye4"
    LEye5 = "LEye5"
    OMouth0 = "OMouth0"
    OMouth1 = "OMouth1"
    OMouth2 = "OMouth2"
    OMouth3 = "OMouth3"
    OMouth4 = "OMouth4"
    OMouth5 = "OMouth5"
    OMouth6 = "OMouth6"
    OMouth7 = "OMouth7"
    OMouth8 = "OMouth8"
    OMouth9 = "OMouth9"
    OMouth10 = "OMouth10"
    OMouth11 = "OMouth11"
    IMouth0 = "IMouth0"
    IMouth1 = "IMouth1"
    IMouth2 = "IMouth2"
    IMouth3 = "IMouth3"
    IMouth4 = "IMouth4"
    IMouth5 = "IMouth5"
    IMouth6 = "IMouth6"
    IMouth7 = "IMouth7"
    RPupil = "RPupil"
    LPupil = "LPupil"


body_skeleton = [
    [KPId.left_ear, KPId.left_eye, KPId.nose, KPId.right_eye, KPId.right_ear,],
    [KPId.left_wrist, KPId.left_elbow, KPId.left_elbow, KPId.left_shoulder,
     KPId.neck,
     KPId.right_shoulder, KPId.right_elbow, KPId.right_wrist,],
    [KPId.nose, KPId.neck, KPId.mid_hip,],
    [KPId.left_ankle, KPId.left_knee, KPId.left_hip,
    KPId.mid_hip,
    KPId.right_hip, KPId.right_knee, KPId.right_ankle,],
    [KPId.left_bigtoe, KPId.left_smalltoe, KPId.left_ankle, KPId.left_heel,],
    [KPId.right_bigtoe, KPId.right_smalltoe, KPId.right_ankle, KPId.right_heel,],
]


left_hand_skeleton = [
    [KPId.LWristBase, KPId.LThumb1CMC, KPId.LThumb2Knuckles, KPId.LThumb3IP, KPId.LThumb4FingerTip,],
    [KPId.LWristBase, KPId.LIndex1Knuckles, KPId.LIndex2PIP, KPId.LIndex3DIP, KPId.LIndex4FingerTip,],
    [KPId.LWristBase, KPId.LMiddle1Knuckles, KPId.LMiddle2PIP, KPId.LMiddle3DIP, KPId.LMiddle4FingerTip,],
    [KPId.LWristBase, KPId.LRing1Knuckles, KPId.LRing2PIP, KPId.LRing3DIP, KPId.LRing4FingerTip,],
    [KPId.LWristBase, KPId.LPinky1Knuckles, KPId.LPinky2PIP, KPId.LPinky3DIP, KPId.LPinky4FingerTip,],
]


right_hand_skeleton = [
    [KPId.RWristBase, KPId.RThumb1CMC, KPId.RThumb2Knuckles, KPId.RThumb3IP, KPId.RThumb4FingerTip,],
    [KPId.RWristBase, KPId.RIndex1Knuckles, KPId.RIndex2PIP, KPId.RIndex3DIP, KPId.RIndex4FingerTip,],
    [KPId.RWristBase, KPId.RMiddle1Knuckles, KPId.RMiddle2PIP, KPId.RMiddle3DIP, KPId.RMiddle4FingerTip,],
    [KPId.RWristBase, KPId.RRing1Knuckles, KPId.RRing2PIP, KPId.RRing3DIP, KPId.RRing4FingerTip,],
    [KPId.RWristBase, KPId.RPinky1Knuckles, KPId.RPinky2PIP, KPId.RPinky3DIP, KPId.RPinky4FingerTip,],
]

face_skeleton = [
    [KPId.FaceContour0, KPId.FaceContour1, KPId.FaceContour2, KPId.FaceContour3, KPId.FaceContour4, KPId.FaceContour5,
     KPId.FaceContour6, KPId.FaceContour7, KPId.FaceContour8, KPId.FaceContour9, KPId.FaceContour10, KPId.FaceContour11,
     KPId.FaceContour12, KPId.FaceContour13, KPId.FaceContour14, KPId.FaceContour15, KPId.FaceContour16,],
    [KPId.REyeBrow0, KPId.REyeBrow1, KPId.REyeBrow2, KPId.REyeBrow3, KPId.REyeBrow4,],
    [KPId.LEyeBrow4, KPId.LEyeBrow3, KPId.LEyeBrow2, KPId.LEyeBrow1, KPId.LEyeBrow0,],
    [KPId.NoseUpper0, KPId.NoseUpper1, KPId.NoseUpper2, KPId.NoseUpper3,],
    [KPId.NoseLower0, KPId.NoseLower1, KPId.NoseLower2, KPId.NoseLower3, KPId.NoseLower4,],
    [KPId.REye0, KPId.REye1, KPId.REye2, KPId.REye3, KPId.REye4, KPId.REye5,],
    [KPId.LEye0, KPId.LEye1, KPId.LEye2, KPId.LEye3, KPId.LEye4, KPId.LEye5,],
    [KPId.OMouth0, KPId.OMouth1, KPId.OMouth2, KPId.OMouth3, KPId.OMouth4, KPId.OMouth5, KPId.OMouth6, KPId.OMouth7,
     KPId.OMouth8, KPId.OMouth9, KPId.OMouth10, KPId.OMouth11,],
    [KPId.IMouth0, KPId.IMouth1, KPId.IMouth2, KPId.IMouth3, KPId.IMouth4, KPId.IMouth5, KPId.IMouth6, KPId.IMouth7,],
# KPId.RPupil,
# KPId.LPupil,
]


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
        "and 1.0 means the extreme right edge of the image",
    )
    y: float = Field(
        title="Relative Y-Coordinate",
        description="Represented as a float in the range [0.0,1.0], "
        "where 0.0 means the extreme top edge of the image"
        "and 1.0 means the extreme bottom edge of the image",
    )
    confidence: float = Field(
        title="confidence in the point accuracy",
        description="Represented as a float in the range [0.0,1.0], "
        "where 0.0 means completely uncertain"
        "and 1.0 means complete confidence / 'certainty'",
    )


class Keypoint(Point):
    id: KPId


class Pose(BaseModel):
    def get_keypoint(self, kpid: KPId) -> Keypoint:
        return self.__getattribute__(kpid)


class BodyPose(Pose):
    """
    Detected location (relative image coordinates) of 25 main body joints / key-points.
    """
    _skeleton = body_skeleton

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
    def from_keypoints(keypoints: List[Keypoint]) -> "BodyPose":
        points = dict([(kpt.id, kpt) for kpt in keypoints])
        return BodyPose(**points)


class LeftHandPose(Pose):
    """
    Detected location (relative image coordinates) of left hand joints / key-points.
    """
    _skeleton = left_hand_skeleton

    LWristBase: Optional[Point] = Field(title="Location of the LWristBase")
    LThumb1CMC: Optional[Point] = Field(title="Location of the LThumb1CMC")
    LThumb2Knuckles: Optional[Point] = Field(title="Location of the LThumb2Knuckles")
    LThumb3IP: Optional[Point] = Field(title="Location of the LThumb3IP")
    LThumb4FingerTip: Optional[Point] = Field(title="Location of the LThumb4FingerTip")
    LIndex1Knuckles: Optional[Point] = Field(title="Location of the LIndex1Knuckles")
    LIndex2PIP: Optional[Point] = Field(title="Location of the LIndex2PIP")
    LIndex3DIP: Optional[Point] = Field(title="Location of the LIndex3DIP")
    LIndex4FingerTip: Optional[Point] = Field(title="Location of the LIndex4FingerTip")
    LMiddle1Knuckles: Optional[Point] = Field(title="Location of the LMiddle1Knuckles")
    LMiddle2PIP: Optional[Point] = Field(title="Location of the LMiddle2PIP")
    LMiddle3DIP: Optional[Point] = Field(title="Location of the LMiddle3DIP")
    LMiddle4FingerTip: Optional[Point] = Field(title="Location of the LMiddle4FingerTip")
    LRing1Knuckles: Optional[Point] = Field(title="Location of the LRing1Knuckles")
    LRing2PIP: Optional[Point] = Field(title="Location of the LRing2PIP")
    LRing3DIP: Optional[Point] = Field(title="Location of the LRing3DIP")
    LRing4FingerTip: Optional[Point] = Field(title="Location of the LRing4FingerTip")
    LPinky1Knuckles: Optional[Point] = Field(title="Location of the LPinky1Knuckles")
    LPinky2PIP: Optional[Point] = Field(title="Location of the LPinky2PIP")
    LPinky3DIP: Optional[Point] = Field(title="Location of the LPinky3DIP")
    LPinky4FingerTip: Optional[Point] = Field(title="Location of the LPinky4FingerTip")

    @staticmethod
    def from_keypoints(keypoints: List[Keypoint]) -> "LeftHandPose":
        points = dict([(kpt.id, kpt) for kpt in keypoints])
        return LeftHandPose(**points)


class RightHandPose(Pose):
    """
    Detected location (relative image coordinates) of right hand joints / key-points.
    """
    _skeleton = right_hand_skeleton

    RWristBase: Optional[Point] = Field(title="Location of the RWristBase")
    RThumb1CMC: Optional[Point] = Field(title="Location of the RThumb1CMC")
    RThumb2Knuckles: Optional[Point] = Field(title="Location of the RThumb2Knuckles")
    RThumb3IP: Optional[Point] = Field(title="Location of the RThumb3IP")
    RThumb4FingerTip: Optional[Point] = Field(title="Location of the RThumb4FingerTip")
    RIndex1Knuckles: Optional[Point] = Field(title="Location of the RIndex1Knuckles")
    RIndex2PIP: Optional[Point] = Field(title="Location of the RIndex2PIP")
    RIndex3DIP: Optional[Point] = Field(title="Location of the RIndex3DIP")
    RIndex4FingerTip: Optional[Point] = Field(title="Location of the RIndex4FingerTip")
    RMiddle1Knuckles: Optional[Point] = Field(title="Location of the RMiddle1Knuckles")
    RMiddle2PIP: Optional[Point] = Field(title="Location of the RMiddle2PIP")
    RMiddle3DIP: Optional[Point] = Field(title="Location of the RMiddle3DIP")
    RMiddle4FingerTip: Optional[Point] = Field(title="Location of the RMiddle4FingerTip")
    RRing1Knuckles: Optional[Point] = Field(title="Location of the RRing1Knuckles")
    RRing2PIP: Optional[Point] = Field(title="Location of the RRing2PIP")
    RRing3DIP: Optional[Point] = Field(title="Location of the RRing3DIP")
    RRing4FingerTip: Optional[Point] = Field(title="Location of the RRing4FingerTip")
    RPinky1Knuckles: Optional[Point] = Field(title="Location of the RPinky1Knuckles")
    RPinky2PIP: Optional[Point] = Field(title="Location of the RPinky2PIP")
    RPinky3DIP: Optional[Point] = Field(title="Location of the RPinky3DIP")
    RPinky4FingerTip: Optional[Point] = Field(title="Location of the RPinky4FingerTip")

    @staticmethod
    def from_keypoints(keypoints: List[Keypoint]) -> "RightHandPose":
        points = dict([(kpt.id, kpt) for kpt in keypoints])
        return RightHandPose(**points)


class FacePose(Pose):
    """
    Detected location (relative image coordinates) of 70 face key-points.
    """
    _skeleton = face_skeleton

    FaceContour0: Optional[Point] = Field(title="Location of the FaceContour0")
    FaceContour1: Optional[Point] = Field(title="Location of the FaceContour1")
    FaceContour2: Optional[Point] = Field(title="Location of the FaceContour2")
    FaceContour3: Optional[Point] = Field(title="Location of the FaceContour3")
    FaceContour4: Optional[Point] = Field(title="Location of the FaceContour4")
    FaceContour5: Optional[Point] = Field(title="Location of the FaceContour5")
    FaceContour6: Optional[Point] = Field(title="Location of the FaceContour6")
    FaceContour7: Optional[Point] = Field(title="Location of the FaceContour7")
    FaceContour8: Optional[Point] = Field(title="Location of the FaceContour8")
    FaceContour9: Optional[Point] = Field(title="Location of the FaceContour9")
    FaceContour10: Optional[Point] = Field(title="Location of the FaceContour10")
    FaceContour11: Optional[Point] = Field(title="Location of the FaceContour11")
    FaceContour12: Optional[Point] = Field(title="Location of the FaceContour12")
    FaceContour13: Optional[Point] = Field(title="Location of the FaceContour13")
    FaceContour14: Optional[Point] = Field(title="Location of the FaceContour14")
    FaceContour15: Optional[Point] = Field(title="Location of the FaceContour15")
    FaceContour16: Optional[Point] = Field(title="Location of the FaceContour16")
    REyeBrow0: Optional[Point] = Field(title="Location of the REyeBrow0")
    REyeBrow1: Optional[Point] = Field(title="Location of the REyeBrow1")
    REyeBrow2: Optional[Point] = Field(title="Location of the REyeBrow2")
    REyeBrow3: Optional[Point] = Field(title="Location of the REyeBrow3")
    REyeBrow4: Optional[Point] = Field(title="Location of the REyeBrow4")
    LEyeBrow4: Optional[Point] = Field(title="Location of the LEyeBrow4")
    LEyeBrow3: Optional[Point] = Field(title="Location of the LEyeBrow3")
    LEyeBrow2: Optional[Point] = Field(title="Location of the LEyeBrow2")
    LEyeBrow1: Optional[Point] = Field(title="Location of the LEyeBrow1")
    LEyeBrow0: Optional[Point] = Field(title="Location of the LEyeBrow0")
    NoseUpper0: Optional[Point] = Field(title="Location of the NoseUpper0")
    NoseUpper1: Optional[Point] = Field(title="Location of the NoseUpper1")
    NoseUpper2: Optional[Point] = Field(title="Location of the NoseUpper2")
    NoseUpper3: Optional[Point] = Field(title="Location of the NoseUpper3")
    NoseLower0: Optional[Point] = Field(title="Location of the NoseLower0")
    NoseLower1: Optional[Point] = Field(title="Location of the NoseLower1")
    NoseLower2: Optional[Point] = Field(title="Location of the NoseLower2")
    NoseLower3: Optional[Point] = Field(title="Location of the NoseLower3")
    NoseLower4: Optional[Point] = Field(title="Location of the NoseLower4")
    REye0: Optional[Point] = Field(title="Location of the REye0")
    REye1: Optional[Point] = Field(title="Location of the REye1")
    REye2: Optional[Point] = Field(title="Location of the REye2")
    REye3: Optional[Point] = Field(title="Location of the REye3")
    REye4: Optional[Point] = Field(title="Location of the REye4")
    REye5: Optional[Point] = Field(title="Location of the REye5")
    LEye0: Optional[Point] = Field(title="Location of the LEye0")
    LEye1: Optional[Point] = Field(title="Location of the LEye1")
    LEye2: Optional[Point] = Field(title="Location of the LEye2")
    LEye3: Optional[Point] = Field(title="Location of the LEye3")
    LEye4: Optional[Point] = Field(title="Location of the LEye4")
    LEye5: Optional[Point] = Field(title="Location of the LEye5")
    OMouth0: Optional[Point] = Field(title="Location of the OMouth0")
    OMouth1: Optional[Point] = Field(title="Location of the OMouth1")
    OMouth2: Optional[Point] = Field(title="Location of the OMouth2")
    OMouth3: Optional[Point] = Field(title="Location of the OMouth3")
    OMouth4: Optional[Point] = Field(title="Location of the OMouth4")
    OMouth5: Optional[Point] = Field(title="Location of the OMouth5")
    OMouth6: Optional[Point] = Field(title="Location of the OMouth6")
    OMouth7: Optional[Point] = Field(title="Location of the OMouth7")
    OMouth8: Optional[Point] = Field(title="Location of the OMouth8")
    OMouth9: Optional[Point] = Field(title="Location of the OMouth9")
    OMouth10: Optional[Point] = Field(title="Location of the OMouth10")
    OMouth11: Optional[Point] = Field(title="Location of the OMouth11")
    IMouth0: Optional[Point] = Field(title="Location of the IMouth0")
    IMouth1: Optional[Point] = Field(title="Location of the IMouth1")
    IMouth2: Optional[Point] = Field(title="Location of the IMouth2")
    IMouth3: Optional[Point] = Field(title="Location of the IMouth3")
    IMouth4: Optional[Point] = Field(title="Location of the IMouth4")
    IMouth5: Optional[Point] = Field(title="Location of the IMouth5")
    IMouth6: Optional[Point] = Field(title="Location of the IMouth6")
    IMouth7: Optional[Point] = Field(title="Location of the IMouth7")
    RPupil: Optional[Point] = Field(title="Location of the RPupil")
    LPupil: Optional[Point] = Field(title="Location of the LPupil")

    @staticmethod
    def from_keypoints(keypoints: List[Keypoint]) -> "FacePose":
        points = dict([(kpt.id, kpt) for kpt in keypoints])
        return FacePose(**points)


class Person(BaseModel):
    """
    Representation of a detected person, including:

    - estimated age (disabled)
    - estimated gender (disabled)
    - pose
    - left and right hand
    - face
    """
    bounding_box: Optional[Tuple[float, float, float, float]] = Field(title="Object bounding box x1y1x2y2")

    gender: Optional[float] = Field(
        title="Estimated gender, if enabled.",
        description="Represented as a float in the range [-1.0,1.0], "
        "where -1.0 means confidently male"
        "and 1.0 means confidently female"
        "and numbers close to 0.0 means uncertain",
    )
    age: Optional[int] = Field(title="Estimated age, if enabled")
    pose: Optional[BodyPose] = Field(title="detected pose key-points")
    left_hand_pose: Optional[LeftHandPose] = Field(title="detected left hand key-points")
    right_hand_pose: Optional[RightHandPose] = Field(title="detected right hand key-points")
    face_pose: Optional[FacePose] = Field(title="detected face key-points")


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
