from pydantic import BaseModel, Field
from datetime import datetime
from typing import Annotated, Literal


class TRzab(BaseModel):
    timestamp: Annotated[
        datetime,
        Field(description="Дата и время измерения (формат ISO или другой, настроенный при импорте)")
    ]
    p_well_depth: Annotated[
        float,
        Field(description="Давление на глубине замера, импортируется")
    ]
    unit_pressure: Annotated[
        Literal['kgc/sm', 'atm', 'Bar'],
        Field(description="Единицы давления")
    ]
    t_well_depth: Annotated[
        float,
        Field(description="Температура на глубине замера в градусах Цельсия")
    ]
    unit_temperature: Annotated[
        Literal['C'],
        Field(default='C', description="Единицы температуры — только °C")
    ]


class Ptp(BaseModel):
    timestamp: Annotated[
        datetime,
        Field(description="Дата и время измерения (формат ISO или другой, настроенный при импорте)")
    ]
    p_well_depth: Annotated[
        float,
        Field(description="Давление в трубном пространстве")
    ]
    unit_pressure: Annotated[
        Literal['kgc/sm', 'atm', 'Bar'],
        Field(description="Единицы давления")
    ]


class Pztp(BaseModel):
    timestamp: Annotated[
        datetime,
        Field(description="Дата и время измерения (формат ISO или другой, настроенный при импорте)")
    ]
    p_well_depth: Annotated[
        float,
        Field(description="Давление в затрубном пространстве")
    ]
    unit_pressure: Annotated[
        Literal['kgc/sm', 'atm', 'Bar'],
        Field(description="Единицы давления")
    ]


class Plin(BaseModel):
    timestamp: Annotated[
        datetime,
        Field(description="Дата и время измерения (формат ISO или другой, настроенный при импорте)")
    ]
    p_well_depth: Annotated[
        float,
        Field(description="Линейное давление")
    ]
    unit_pressure: Annotated[
        Literal['kgc/sm', 'atm', 'Bar'],
        Field(description="Единицы давления")
    ]


class Debits(BaseModel):
    timestamp: Annotated[
        datetime,
        Field(description="Дата и время измерения (формат ISO или другой, настроенный при импорте)")
    ]
    fluid_flow_rate: Annotated[
        float,
        Field(description="Дебит жидкости")
    ]
    water_cut: Annotated[
        float,
        Field(description="Обводненность)")
    ]
    gas_flow_rate: Annotated[
        float,
        Field(description="Дебит газа)")
    ]


class WellInclinometry(BaseModel):
    measured_depth: Annotated[
        float,
        Field(description="Глубина по стволу)")
    ]
    true_vertical_depth: Annotated[
        float,
        Field(description="Глубина по вертикали)")
    ]
    true_vertical_depth_sub_sea: Annotated[
        float,
        Field(description="Абсолютная отметка)")
    ]