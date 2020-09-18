#!/usr/bin/env python3.8
import logging

from fastapi import FastAPI
from uvicorn import run

from app.routes import pose, status

log = logging.getLogger(__name__)


def create_api() -> FastAPI:
    fast_api = FastAPI()
    fast_api.include_router(status.router, prefix="/status", tags=["status"])
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
