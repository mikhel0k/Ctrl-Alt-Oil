from fastapi import APIRouter

from .productive_horizon.views import router as productive_horizon_router
from .type_of_devices.views import router as type_of_device_router

router = APIRouter()
router.include_router(router=productive_horizon_router, prefix="/reference_books")
router.include_router(router=type_of_device_router, prefix="/reference_books")
