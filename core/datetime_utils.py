from datetime import datetime
from enum import Enum
import re
from pydantic import validators


class DateTimeFormatEnum(str, Enum):
    ISO = "iso"
    TIMESTAMP = "timestamp"
    COUPON = "coupon"
    CUSTOM = "custom"  # DD-MM-YYYY HH:mm
    RAW = "raw"

def validate_datatime(value: str, format_type:DateTimeFormatEnum) -> str:
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

def convert_to_iso(dt_value: str, dt_format: DateTimeFormatEnum) -> str:
    # Конвертация в ISO format
    if dt_format == DateTimeFormatEnum.ISO:
        return datetime.fromisoformat(dt_value).isoformat()
    elif dt_format == DateTimeFormatEnum.TIMESTAMP:
        return datetime.fromtimestamp(float(dt_value)).isoformat()
    elif dt_format == DateTimeFormatEnum.COUPON:
        date_part = dt_value.split('-')[0]
        return datetime.strptime(date_part, "%d%b%Y").isoformat()
    elif dt_format == DateTimeFormatEnum.CUSTOM:
        return datetime.strptime(dt_value, "%d-%m-%Y %H:%M").isoformat()
    elif dt_format == DateTimeFormatEnum.RAW:
        return dt_value  # Сохраняем как есть