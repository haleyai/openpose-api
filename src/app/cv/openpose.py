from functools import lru_cache
from app.schemas.pose import KPId, Keypoint, Pose, LeftHandPose, RightHandPose, FacePose, Person
from typing import List
from app.cv.engine import Engine
from itertools import zip_longest
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

# taken from https://github.com/AmitMY/pose-format/blob/c669f7bcb851a7ecdbce7ad35add46b3a1196d31/pose_format/utils/openpose_135.py

openpose_left_hand_keypoints = [
    KPId.LWristBase,
    KPId.LThumb1CMC, 
    KPId.LThumb2Knuckles, 
    KPId.LThumb3IP, 
    KPId.LThumb4FingerTip, 
    KPId.LIndex1Knuckles, 
    KPId.LIndex2PIP,
    KPId.LIndex3DIP, 
    KPId.LIndex4FingerTip, 
    KPId.LMiddle1Knuckles, 
    KPId.LMiddle2PIP, 
    KPId.LMiddle3DIP,
    KPId.LMiddle4FingerTip, 
    KPId.LRing1Knuckles, 
    KPId.LRing2PIP, 
    KPId.LRing3DIP, 
    KPId.LRing4FingerTip,
    KPId.LPinky1Knuckles, 
    KPId.LPinky2PIP, 
    KPId.LPinky3DIP, 
    KPId.LPinky4FingerTip,
]

openpose_right_hand_keypoints = [
    KPId.RWristBase,
    KPId.RThumb1CMC, 
    KPId.RThumb2Knuckles, 
    KPId.RThumb3IP, 
    KPId.RThumb4FingerTip, 
    KPId.RIndex1Knuckles,
    KPId.RIndex2PIP,
    KPId.RIndex3DIP, 
    KPId.RIndex4FingerTip, 
    KPId.RMiddle1Knuckles, 
    KPId.RMiddle2PIP, 
    KPId.RMiddle3DIP,
    KPId.RMiddle4FingerTip, 
    KPId.RRing1Knuckles, 
    KPId.RRing2PIP, 
    KPId.RRing3DIP, 
    KPId.RRing4FingerTip,
    KPId.RPinky1Knuckles, 
    KPId.RPinky2PIP, 
    KPId.RPinky3DIP, 
    KPId.RPinky4FingerTip,
]

openpose_face_keypoints = [
    KPId.FaceContour0, 
    KPId.FaceContour1, 
    KPId.FaceContour2,
    KPId.FaceContour3, 
    KPId.FaceContour4,
    KPId.FaceContour5,
    KPId.FaceContour6, 
    KPId.FaceContour7, 
    KPId.FaceContour8, 
    KPId.FaceContour9, 
    KPId.FaceContour10,
    KPId.FaceContour11,
    KPId.FaceContour12, 
    KPId.FaceContour13, 
    KPId.FaceContour14, 
    KPId.FaceContour15, 
    KPId.FaceContour16,
    KPId.REyeBrow0, 
    KPId.REyeBrow1, 
    KPId.REyeBrow2, 
    KPId.REyeBrow3,
    KPId.REyeBrow4, 
    KPId.LEyeBrow4, 
    KPId.LEyeBrow3,
    KPId.LEyeBrow2,
    KPId.LEyeBrow1,
    KPId.LEyeBrow0, 
    KPId.NoseUpper0, 
    KPId.NoseUpper1, 
    KPId.NoseUpper2, 
    KPId.NoseUpper3, 
    KPId.NoseLower0,
    KPId.NoseLower1,
    KPId.NoseLower2,
    KPId.NoseLower3, 
    KPId.NoseLower4, 
    KPId.REye0,
    KPId.REye1,
    KPId.REye2, 
    KPId.REye3,
    KPId.REye4,
    KPId.REye5, 
    KPId.LEye0,
    KPId.LEye1, 
    KPId.LEye2, 
    KPId.LEye3,
    KPId.LEye4,
    KPId.LEye5, 
    KPId.OMouth0,
    KPId.OMouth1,
    KPId.OMouth2, 
    KPId.OMouth3,
    KPId.OMouth4,
    KPId.OMouth5, 
    KPId.OMouth6, 
    KPId.OMouth7, 
    KPId.OMouth8, 
    KPId.OMouth9, 
    KPId.OMouth10,
    KPId.OMouth11,
    KPId.IMouth0,
    KPId.IMouth1,
    KPId.IMouth2,
    KPId.IMouth3, 
    KPId.IMouth4, 
    KPId.IMouth5, 
    KPId.IMouth6, 
    KPId.IMouth7,
    KPId.RPupil, 
    KPId.LPupil,
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

    @staticmethod
    def __keypoints_from_array(keypoints_array, openpose_keypoints, width, height):
        persons = []
        for openpose_object in keypoints_array:
            keypoints = []
            for ix, detected_kpt in enumerate(openpose_object):
                if len(detected_kpt) == 3 and detected_kpt[2] > 0.0:
                    keypoints.append(
                        Keypoint(
                            id=openpose_keypoints[ix],
                            x=detected_kpt[0] / width,
                            y=detected_kpt[1] / height,
                            confidence=detected_kpt[2],
                        )
                    )
            persons.append(keypoints)
        return persons

    def infer_image(self, image) -> List[Person]:
        print("inferring from image")
        if image is None:
            print("no image :(")
            return []

        height, width, _ = np.shape(image)

        datum = op.Datum()
        datum.cvInputData = image
        self._opWrapper.emplaceAndPop(op.VectorDatum([datum]))

        poses = [
            Pose.from_keypoints(keypoints=keypoints)
            for keypoints in
            self.__keypoints_from_array(
                 datum.poseKeypoints,
                 openpose_keypoints,
                 width,
                 height)
            ]
        left_hand_poses = [
            LeftHandPose.from_keypoints(keypoints=keypoints)
            for keypoints in
            self.__keypoints_from_array(
                datum.handKeypoints[0],
                openpose_left_hand_keypoints,
                width,
                height)
        ]
        right_hand_poses = [
            RightHandPose.from_keypoints(keypoints=keypoints)
            for keypoints in
            self.__keypoints_from_array(
                datum.handKeypoints[1],
                openpose_right_hand_keypoints,
                width,
                height)
        ]
        face_poses = [
            FacePose.from_keypoints(keypoints=keypoints)
            for keypoints in
            self.__keypoints_from_array(
                datum.faceKeypoints,
                openpose_face_keypoints,
                width,
                height)
        ]
        return [
            Person(pose=pose, left_hand_pose=lhand, right_hand_pose=rhand, face_pose=face)
            for pose, lhand, rhand, face in
            zip_longest(poses, left_hand_poses, right_hand_poses, face_poses, fillvalue=None)
        ]


engine = OpenPoseEngine(face=True, hand=True)


@lru_cache()
def get_openpose_engine():
    return engine
