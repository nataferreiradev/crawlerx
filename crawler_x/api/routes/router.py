from fastapi import APIRouter
from .api_routes import router as api_router
from .script_routes import router as script_router
from .data_recover_routes import router as data_recover_router
from .crawler_routes import router as crawler_router
from .logs import router as log_router

router = APIRouter()

router.include_router(api_router, prefix="/api", tags=["API"])
router.include_router(script_router, prefix="/script", tags=["Script"])
router.include_router(data_recover_router, prefix="/dataRecover", tags=["Data Recover"])
router.include_router(crawler_router, prefix="/crawler", tags=["Crawler"])
router.include_router(log_router,prefix="/logs",tags=["logs"])