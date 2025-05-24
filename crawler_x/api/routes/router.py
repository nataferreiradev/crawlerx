from fastapi import APIRouter
from .api_routes import router as api_router
from .script_routes import router as script_router
from .data_recover_routes import router as data_recover_router

router = APIRouter()

router.include_router(api_router, prefix="/api", tags=["API"])
router.include_router(script_router, prefix="/script", tags=["Script"])
router.include_router(data_recover_router, prefix="/dataRecover", tags=["Data Recover"])