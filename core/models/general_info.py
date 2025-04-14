from sqlalchemy.orm import Mapped

from .base import Base


class ProductiveHorizon(Base):
    __tablename__ = 'ProductiveHorizon'

    productive_horizon: Mapped[str]


class NameOfDeposits(Base):
    __tablename__ = 'NameOfDeposits'

    name_of_deposits: Mapped[str]


class TypeOfDevices(Base):
    __tablename__ = 'TypeOfDevices'

    type_of_devices: Mapped[str]
