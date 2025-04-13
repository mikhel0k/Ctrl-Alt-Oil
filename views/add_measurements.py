from fastapi import APIRouter

from schemas.measurements import TRzab, Ptp, Pztp, Plin, Debits, WellInclinometry


router = APIRouter(prefix="/add/loading", tags=['loading'])


@router.post("/TRzab")
def Loading_TRzab(data: TRzab):
    return data


@router.post("/Ptp")
def Loading_Ptp(data: Ptp):
    return Ptp


@router.post("/Pztp")
def Loading_Pztp(data: Pztp):
    return Pztp


@router.post("/Plin")
def Loading_Plin(data: Plin):
    return Plin


@router.post("/debits")
def Loading_Debits(data: Debits):
    return Debits


@router.post("/well_inclinometry")
def Loading_Well_Inclinometry(data: WellInclinometry):
    return WellInclinometry
