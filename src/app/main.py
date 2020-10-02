#!/usr/bin/env python3.8
import logging

from fastapi import FastAPI
from uvicorn import run

from app.config import get_settings
from app.routes import pose, status

log = logging.getLogger(__name__)


def create_api() -> FastAPI:
    fast_api = FastAPI(
        title="PoseAPI",
        description="""By [Lyngon Pte. Ltd.](https://www.lyngon.com)
        
A basic API for extracting human pose key-points from images.
 
Currently relying on 
[OpenPose from CMU Perceptual Computing Lab](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
as engine. 

Others may come at a later stage.
        """,
        version=get_settings().version,
        openapi_tags=[
            {"name": "pose", "description": "Human Pose Estimation "},
            {"name": "image", "description": "Extract from image"},
            {"name": "url", "description": "Extract from URL"},
            {"name": "draw", "description": "Generate image with key-points drawn"},
            {"name": "util", "description": "Util features"},
        ],
    )
    fast_api.include_router(status.router, prefix="/status", tags=["util"])
    fast_api.include_router(pose.router, prefix="/pose", tags=["pose"])
    return fast_api


api = create_api()


@api.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    # Init of db may go here


@api.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")


# For simplified debug purposes only
if __name__ == "__main__":
    run(api, host="0.0.0.0", port=8000)
