from pydantic import BaseModel, ConfigDict, field_validator
from enum import Enum
from datetime import datetime
import re


class DateTimeFormatEnum(str, Enum):
    ISO = "iso"
    TIMESTAMP = "timestamp"
    COUPON = "coupon"
    CUSTOM = "custom"  # DD-MM-YYYY HH:mm
    RAW = "raw"


class PtpBase(BaseModel):
    DataTime: datetime
    Ptp: float
    DataTimeFormat: DateTimeFormatEnum
    PtpFormat: str

    @field_validator('DataTime')
    def validate_datetime(cls, value, values):
        format_type = values.data.get('DataTimeFormat')

        if format_type == DateTimeFormatEnum.ISO:
            try:
                datetime.fromisoformat(value)
            except ValueError:
                raise ValueError("Invalid ISO format. Use: YYYY-MM-DDTHH:MM:SS")

        elif format_type == DateTimeFormatEnum.TIMESTAMP:
            if not value.replace('.', '', 1).isdigit():
                raise ValueError("Timestamp must be numeric")

        elif format_type == DateTimeFormatEnum.COUPON:
            if not re.match(r"^\d{2}[A-Z]{3}\d{4}-\d{3}$", value):
                raise ValueError("Coupon format: 99XXX9999-999")

        elif format_type == DateTimeFormatEnum.CUSTOM:
            if not re.match(r"^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$", value):
                raise ValueError("Custom format: DD-MM-YYYY HH:mm")

        elif format_type == DateTimeFormatEnum.RAW:
            pass  # No validation

        return value

class PtpCreate(PtpBase):
    pass

class Ptp(PtpBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
