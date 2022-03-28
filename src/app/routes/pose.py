from pydantic import AnyHttpUrl
import io
from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    Body,
)
from starlette.responses import StreamingResponse

from app.cv.fun import infer_url, draw_url, infer_file, draw_file, get_engine
from app.cv.engine import Engine
from app.schemas.pose import Scene


router = APIRouter()


@router.post(
    "/fromurl",
    tags=["url"],
    summary="Image URL to Scene data",
    response_model=Scene,
    response_description="""
### Successful Response: 
A Scene object containing detected objects, such as:

- people: detected people
- vehicles: detected vehicles (disabled)
- things: detected 'things' (disabled) 
""",
)
def extract_pose_from_url(
    *,
    url: AnyHttpUrl = Body(
        ...,
        embed=True,
        title="URL pointing to an image",
        description="Valid URL for a jpeg or png image",
        example="https://upload.wikimedia.org/wikipedia/commons/3/38/Two_dancers.jpg",
    ),
    engine: Engine = Depends(get_engine)
):
    """
    ## Extract Pose From URL
    Extract pose information, from an image URL,

    :param url: URL pointing to an image
    \f
    :param engine: Pose Engine
    :return: A Scene object representing the detected features in the image.
    """
    persons = infer_url(engine, url)
    return Scene(people=persons)


@router.post(
    "/fromurl/draw",
    tags=["url", "draw"],
    summary="Image URL to Image",
    response_description="""
### Successful Response:
A JPEG image with the detected features drawn
""",
)
def draw_pose_from_url(
    *,
    url: AnyHttpUrl = Body(
        ...,
        embed=True,
        title="URL pointing to an image",
        description="Valid URL for a jpeg or png image",
        example="https://upload.wikimedia.org/wikipedia/commons/3/38/Two_dancers.jpg",
    ),
    engine: Engine = Depends(get_engine)
):
    """
    ## Draw Pose From URL
    Create a ned image with scene (pose) information drawn, from an image URL,

    :param url: URL pointing to an image
    \f
    :param engine: Pose Engine
    :return: A JPEG image with the detected features drawn
    """
    image = draw_url(engine, url)
    return StreamingResponse(io.BytesIO(image), media_type="image/jpg")


@router.post(
    "/fromfile/",
    tags=["image"],
    summary="Image to Scene data",
    response_model=Scene,
    response_description="""
### Successful Response: 
A Scene object containing detected objects, such as:

- people: detected people
- vehicles: detected vehicles (disabled)
- things: detected 'things' (disabled) 
""",
)
def extract_pose_from_file(
    *, image_file: UploadFile = File(...), engine: Engine = Depends(get_engine)
):
    """
    ## Extract Pose From Image
    Extract pose information, from an image file,

    :param image_file: An image file (JPEG, PNG)
    \f
    :param engine: Pose Engine
    :return: A Scene object representing the detected features in the image.
    """
    persons = infer_file(engine, image_file)
    return Scene(people=persons)


@router.post(
    "/fromfile/draw",
    tags=["image", "draw"],
    summary="Image to Image",
    response_description="""
### Successful Response:
A JPEG image with the detected features drawn
""",
)
def draw_pose_from_file(
    *, image_file: UploadFile = File(...), engine: Engine = Depends(get_engine)
):
    """
    ## Draw Pose From Image
    Create a ned image with scene (pose) information drawn, from an image file,

    :param image_file: An image file (JPEG, PNG)
    \f
    :param engine: Pose Engine
    :return: A JPEG image with the detected features drawn.
    """
    image = draw_file(engine, image_file)
    return StreamingResponse(io.BytesIO(image), media_type="image/jpg")
