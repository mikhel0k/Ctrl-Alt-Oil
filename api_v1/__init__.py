from fastapi import APIRouter

from .productive_horizon.views import router as productive_horizon_router
from .type_of_devices.views import router as type_of_device_router
from .name_of_deposits.views import router as name_of_deposits
from .ptp.views import router as ptp
from .pztp.views import router as pztp
from .plin.views import router as plin

router = APIRouter()
router.include_router(router=productive_horizon_router, prefix="/reference_books")
router.include_router(router=type_of_device_router, prefix="/reference_books")
router.include_router(router=name_of_deposits, prefix="/reference_books")
router.include_router(router=ptp, prefix="/reference_books")
router.include_router(router=pztp, prefix="/reference_books")
router.include_router(router=plin, prefix="/reference_books")
