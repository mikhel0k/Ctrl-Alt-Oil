from datetime import datetime
from enum import Enum
import re
from pydantic import ValidationError


class DateTimeFormatEnum(str, Enum):
    DEFAULT = "default"  # ДД/ММ/ГГГГ ЧЧ:ММ:СС
    ISO = "iso"
    TIMESTAMP = "timestamp"
    COUPON = "coupon"
    CUSTOM_DASH = "custom_dash"  # DD-MM-YYYY HH:mm
    RAW = "raw"


def validate_datetime(value: str, format_type: DateTimeFormatEnum) -> datetime:
    try:
        if format_type == DateTimeFormatEnum.ISO:
            return datetime.fromisoformat(value)

        elif format_type == DateTimeFormatEnum.TIMESTAMP:
            return datetime.fromtimestamp(float(value))

        elif format_type == DateTimeFormatEnum.COUPON:
            if not re.match(r"^\d{2}[A-Z]{3}\d{4}-\d{3}$", value):
                raise ValueError("Coupon format: 99XXX9999-999")
            date_part = value.split('-')[0]
            return datetime.strptime(date_part, "%d%b%Y")

        elif format_type == DateTimeFormatEnum.DEFAULT:
            if not re.match(r"^\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}$", value):
                raise ValueError("Default format: DD/MM/YYYY HH:mm:ss")
            return datetime.strptime(value, "%d/%m/%Y %H:%M:%S")

        elif format_type == DateTimeFormatEnum.CUSTOM_DASH:
            if not re.match(r"^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$", value):
                raise ValueError("Custom dash format: DD-MM-YYYY HH:mm")
            return datetime.strptime(value, "%d-%m-%Y %H:%M")

        elif format_type == DateTimeFormatEnum.RAW:
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")  # Пример обработки

    except Exception as e:
        raise ValidationError(f"Invalid datetime format: {str(e)}")


def convert_to_iso(dt_value: datetime) -> str:
    return dt_value.isoformat()