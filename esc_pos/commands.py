from abc import ABC, abstractmethod
from build_connections.connections import Connection
from build_connections.connection_adapter import ConnectionAdapter

class Command(ABC):
    _output: bytes

    @property
    def output(self) -> bytes:
        return self._output
    
    @abstractmethod
    def __init__(self):
       pass

    @abstractmethod
    def execute(self, adapt: ConnectionAdapter, *args) -> None:
        pass

class PrintTextCommand(Command):
    def __init__(self):
      super().__init__()

    def execute(self, adapt: ConnectionAdapter, *args) -> None:
        if(len(args) != 1 or not isinstance(args[0], str)):
            raise TypeError("This command accept only one string")
        self._output = adapt.send_text_output(text=args[0])

class PrintImageCommand(Command):
    def __init__(self):
      super().__init__()

    def execute(self, adapt: ConnectionAdapter, *args) -> None:
        if(len(args) != 1 or not isinstance(args[0], bytes)):
            raise TypeError("This command accept image as bytes")
        self._output = adapt.send_image_output(args[0])
    
