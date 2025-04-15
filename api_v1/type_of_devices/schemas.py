from pydantic import BaseModel, ConfigDict


class TypeOfDevicesBase(BaseModel):
    type_of_devices: str


class TypeOfDevicesCreate(TypeOfDevicesBase):
    pass


class TypeOfDevices(TypeOfDevicesBase):
    model_config = ConfigDict(from_attributes=True)

    id: int