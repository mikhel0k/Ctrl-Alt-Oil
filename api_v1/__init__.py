from fastapi import APIRouter

from .productive_horizon.views import router as productive_horizon_router


router = APIRouter()
router.include_router(router=productive_horizon_router, prefix="/reference_books")
