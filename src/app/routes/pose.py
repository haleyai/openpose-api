
from pydantic import AnyUrl
from fastapi import APIRouter
from app.schemas.pose import *


router = APIRouter()


@router.post("/", response_model=Pose)
def extract_pose_from_url(*, url: AnyUrl):
    """
    Create new item.
    """
    return Pose(
        keypoints=[
            Keypoint(
                name=KeypointEnum.left_elbow,
                ix={
                    ModelEnum.openpose: 6,
                    ModelEnum.posenet: 2,
                },
                x=0.211,
                y=0.132,
            ),
            Keypoint(
                name=KeypointEnum.right_ear,
                ix={
                    ModelEnum.openpose: 17,
                    ModelEnum.posenet: 12,
                },
                x=0.120,
                y=0.911,
            ),
        ]
    )

