from schemas.general_info import ProductiveHorizon, NameOfDeposits, TypeOfDevices


def add_productive_horizon(data: ProductiveHorizon):
    productive_horizon = data.model_dump()
    return {"success": True}


def add_name_of_deposits(data: NameOfDeposits):
    name_of_deposits = data.model_dump()
    return {"success": True}


def add_type_of_devices(data: TypeOfDevices):
    type_of_devices = data.model_dump()
    return {"success": True}
