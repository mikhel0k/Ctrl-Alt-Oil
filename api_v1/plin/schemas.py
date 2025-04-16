# schemas.py (исправления)
from pydantic import BaseModel, ConfigDict, field_validator, ValidationError
from datetime import datetime
from core.datetime_utils import validate_datetime, DateTimeFormatEnum


class PlinBase(BaseModel):
    DataTime: datetime
    Plin: float
    DataTimeFormat: DateTimeFormatEnum
    PtpFormat: str

    @field_validator('DataTime', mode='before')
    def validate_ptp_datetime(cls, value, values):
        if not isinstance(value, str):
            return value

        format_type = values.data.get('DataTimeFormat')
        if not format_type:
            raise ValueError("DataTimeFormat is required")

        return validate_datetime(value=value, format_type=format_type)


class PlinCreate(PlinBase):
    pass


class Plin(PlinBase):
    model_config = ConfigDict(from_attributes=True)
    id: int