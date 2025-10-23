from typing import Type, Dict, Any, Callable
from abc import ABC, abstractmethod
from .device import Device
from escpos.printer import Usb, Network, Dummy
from . import constants

# Decorator
def register_connection(key: str) -> Callable[[Type[Connection]], Type[Connection]]:
    def wrapper(conn_cls: Type[Connection]) -> Type[Connection]:
        ConnectionRegistry.register(key, conn_cls)
        return conn_cls
    return wrapper


class Connection(ABC):
    @property
    @abstractmethod
    def printer():
        pass

    @property
    @abstractmethod
    def device(self) -> Device:
        pass

    @abstractmethod
    def init_connection(self, device: Device) -> None:
        pass

class ConnectionRegistry:
    _registry: Dict[str, Type[Connection]] = {}

    @classmethod
    def register(cls, key: str, conn_cls: Type[Connection]) -> None:
        if key in cls._registry:
            raise KeyError(f"Connection key '{key}' already registered")
        cls._registry[key] = conn_cls
        
    @classmethod
    def get(cls, key: str) -> Type[Connection]:
        try:
            return cls._registry[key]
        except KeyError:
            raise KeyError(f"No connection registered for key '{key}'")
        
    @classmethod
    def create(cls, key: str, *args, **kwargs) -> Connection:
        conn_cls = cls.get(key)
        return conn_cls(*args, **kwargs)  

@register_connection("ConnUSB")
class ConnectionUSB(Connection):
    _printer : Usb

    @property
    def printer(self):
        return self._printer

    @property
    def device(self) -> Device:
        return self._device

    def __init__(self, device: Device):
        self.init_connection(device)
    
    def init_connection(self, device: Device) -> None:
        self._device = device
        self._printer = Usb(idVendor=self.device.get_par(constants.VENDOR_ID),
                               idProduct=self.device.get_par(constants.PRODUCT_ID))
        
@register_connection("ConnETH")
class ConnectionETH(Connection):
    _printer : Network

    @property
    def printer(self):
        return self._printer
    
    @property
    def device(self) -> Device:
        return self._device

    def __init__(self, device: Device):
        self.init_connection(device)

    def init_connection(self, device: Device) -> None:
        self._device = device
        port_value = self.device.get_par(constants.PORT)
        port = constants.DEFAULT_PORT if port_value is False else port_value
        self._printer = Network(host=self.device.get_par(constants.IP), port=port)

@register_connection("ConnDummy")
class ConnectionDummy(Connection):
    _printer : Dummy

    @property
    def printer(self):
        return self._printer

    @property
    def device(self) -> Device:
        return self._device

    def __init__(self, device: Device):
        self.init_connection(device)

    def init_connection(self, device: Device) -> None:
        self._device = device
        self._printer = Dummy()