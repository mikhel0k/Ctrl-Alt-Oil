from pydantic import BaseModel, ConfigDict


class NameOfDepositsBase(BaseModel):
    name_of_deposits: str


class NameOfDepositsCreate(NameOfDepositsBase):
    pass


class NameOfDeposits(NameOfDepositsBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
