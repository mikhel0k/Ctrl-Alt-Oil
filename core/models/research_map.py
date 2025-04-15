from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from .base import Base


class Research(Base):
    __tablename__ = "Research"

    field: Mapped[int] = mapped_column(ForeignKey("NameOfDeposits.id"))
    well_number: Mapped[int]
    cluster_site_number: Mapped[int]
    productive_horizon_layer: Mapped[int] = mapped_column(ForeignKey("ProductiveHorizon.id"))
    research_start_date: Mapped[datetime]
    research_end_date: Mapped[datetime]
    device_type: Mapped[int] = mapped_column(ForeignKey("TypeOfDevices.id"))
    device_number: Mapped[int]

    instrument_depth_tvd: Mapped[float]
    instrument_depth_tvdss: Mapped[float]

    perforation_top_md: Mapped[float]
    perforation_top_tvd: Mapped[float]
    perforation_top_tvdss: Mapped[float]

    depth_difference_instrument_perforation: Mapped[float]
    oil_flow_correction_density: Mapped[float]
    fluid_density_vdp_shutdown: Mapped[float]
    fluid_density_vdp_operating: Mapped[float]
    pressure_difference_depth_vdp_shutdown: Mapped[float]
    pressure_difference_depth_vdp_operating: Mapped[float]
