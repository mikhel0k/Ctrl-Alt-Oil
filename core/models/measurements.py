from sqlalchemy.orm import Mapped
from datetime import datetime
from .base import Base


class TRzab(Base):
    __tablename__ = "TRzab"

    data_time: Mapped[datetime]
    rzab: Mapped[int]
    rzab_vpd: Mapped[int]
    tzab: Mapped[int]
    rzab_format: Mapped[int]


class Ptp(Base):
    __tablename__ = "Ptp"

    data_time: Mapped[datetime]
    ptp: Mapped[float]
    data_time_format: Mapped[str]
    ptp_format: Mapped[str]


class Pztp(Base):
    __tablename__ = "Pztp"

    data_time: Mapped[datetime]
    pztp: Mapped[float]
    data_time_format: Mapped[str]
    pztp_format: Mapped[str]


class Plin(Base):
    __tablename__ = "Plin"

    data_time: Mapped[datetime]
    plin: Mapped[float]
    data_time_format: Mapped[str]
    plin_format: Mapped[str]


class Debits(Base):
    __tablename__ = "Debits"

    data_time: Mapped[datetime]
    fluid_flow_rate: Mapped[float]
    oil_flow_rate: Mapped[float]
    water_flow_rate: Mapped[float]
    water_cut: Mapped[float]
    gas_flow_rate: Mapped[float]
    gase_factor: Mapped[int]
    data_time_format: Mapped[str]


class WellInclinometry(Base):
    __tablename__ = "WellInclinometry"

    measured_depth: Mapped[float]
    true_vertical_depth: Mapped[float]
    true_vertical_depth_sub_sea: Mapped[float]
