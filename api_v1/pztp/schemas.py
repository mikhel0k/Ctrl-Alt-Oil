from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime

from core.datetime_utils import validate_datatime, DateTimeFormatEnum


class PztpBase(BaseModel):
    DataTime: datetime
    Pztp: float
    DataTimeFormat: DateTimeFormatEnum
    PtpFormat: str

    @field_validator('DataTime')
    def validate_ptp_datetime(cls, value, values):
        format_type = values.data.get('DataTimeFormat')
        return validate_datatime(value=value, format_type=format_type)

class PztpCreate(PztpBase):
    pass

class Pztp(PztpBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
