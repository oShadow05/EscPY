from abc import ABC, abstractmethod

class DeviceParamsBag:
    _params : dict[str, str | int | float]

    @property
    def params(self) -> dict[str, str | int | float]:
        return self._params

    def __init__(self):
        self._params = {}

    def add_par_str(self, key: str, parameter: str) -> DeviceParamsBag:
        self._params[key] = parameter
        return self

    def add_par_int(self, key: str, parameter: int) -> DeviceParamsBag:
        self._params[key] = parameter
        return self
        
    def add_par_float(self, key: str, parameter: float) -> DeviceParamsBag:
        self._params[key] = parameter
        return self
    
    def clear(self) -> DeviceParamsBag:
        self._params = {}
        return self
    
    def retrieve(self, key: str):
        return self.params.get(key, False)

class Device:
    name: str
    _device_params: DeviceParamsBag
    
    def get_par(self, key: str):
        return self._device_params.retrieve(key)
    
    def __init__(self, name: str, device_params: DeviceParamsBag):
        self.name = name
        self._device_params = device_params
