from pydantic import AnyUrl
import io
from fastapi import APIRouter, Depends
from starlette.responses import StreamingResponse
from app.cv.openpose import OpenPoseEngine, get_openpose_engine

from app.cv.fun import infer_url, draw_url
from typing import List
from app.schemas.pose import Pose


router = APIRouter()


@router.post("/", response_model=List[Pose])
def extract_pose_from_url(*, url: AnyUrl, engine: OpenPoseEngine = Depends(get_openpose_engine)):
    """
    \f
    :param url:
    :param engine:
    :return:
    """
    return infer_url(engine, url)


@router.post("/draw")
def draw_pose_from_url(*, url: AnyUrl, engine: OpenPoseEngine = Depends(get_openpose_engine)):
    """
    \f
    :param url:
    :param engine:
    :return:
    """
    image = draw_url(engine, url)

    return StreamingResponse(io.BytesIO(image), media_type="image/jpg")
