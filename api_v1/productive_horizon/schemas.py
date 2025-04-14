from pydantic import BaseModel, ConfigDict


class ProductiveHorizonBase(BaseModel):
    productive_horizon: str


class ProductiveHorizonCreate(ProductiveHorizonBase):
    pass


class ProductiveHorizon(ProductiveHorizonBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
