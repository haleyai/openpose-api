from fastapi import APIRouter, Depends
from app.config import get_settings, Settings

router = APIRouter()


@router.get(
    "/",
    summary="Retrieve deployment information",
    response_description="""A JSON object containing deployment information:
    
- version: API version
- status: run-status of deployment
- environment: name of deployment environment
- testing: Boolean indicating if testing options are enabled
    """,
)
async def status(settings: Settings = Depends(get_settings)):
    """
### Retrieve API deployment status

- version: API version
- status: run-status of deployment
- environment: name of deployment environment
- testing: Boolean indicating if testing options are enabled
    """
    return {
        "version": settings.version,
        "status": "running",
        "environment": settings.environment,
        "testing": settings.testing,
    }
