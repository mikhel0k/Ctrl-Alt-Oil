from pydantic import BaseModel, Field
from typing import Annotated
from annotated_types import MinLen


class ProductiveHorizon(BaseModel):
    productive_horizon: Annotated[
        str,
        MinLen(2),
        Field(description="Продуктивный горизонт, пласт"),
    ]


class NameOfDeposits(BaseModel):
    name_of_deposits: Annotated[
        str,
        MinLen(3),
        Field(description="Месторождение / Лицензионный участок недр"),
    ]


class TypeOfDevices(BaseModel):
    type_of_devices: Annotated[
        str,
        MinLen(3),
        Field(description="Прибор")
    ]
