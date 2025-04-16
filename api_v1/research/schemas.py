from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ResearchBase(BaseModel):
    field: int
    well_number: int
    cluster_site_number: int
    productive_horizon_layer: int
    research_start_date: datetime
    research_end_date: datetime
    device_type: int
    device_number: int

    instrument_depth_tvd: float
    instrument_depth_tvdss: float

    perforation_top_md: float
    perforation_top_tvd: float
    perforation_top_tvdss: float

    depth_difference_instrument_perforation: float
    oil_flow_correction_density: float
    fluid_density_vdp_shutdown: float
    fluid_density_vdp_operating: float
    pressure_difference_depth_vdp_shutdown: float
    pressure_difference_depth_vdp_operating: float


class ResearchCreate(ResearchBase):
    pass

class Research(ResearchBase):
    model_config = ConfigDict(from_attributes=True)

    id: int

class ResearchFour(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    field: int
    research_start_date: datetime
    research_end_date: datetime
    id: int
