from abc import ABC, abstractmethod
from ...Utility.Debug import Debug

class BaseState(ABC):
    def __init__(self, name, canSwitchTO=None, pointerTOScript=None, **kwargs):
        Debug.log("BaseState __init__", "Header", group="LIB")
        self.name = name
        self.canSwitchTO = canSwitchTO or []
        self.pointerTOScript = pointerTOScript
        Debug.log(f"BaseState {self.name} initialized", "Info", group="LIB")
        Debug.log("BaseState __init__", "End", group="LIB")

    def __call__(self, **kwargs):
        """Allow state() to trigger an update."""
        self.Update(**kwargs)

    @abstractmethod
    def Enter(self, **kwargs):
        pass

    @abstractmethod
    def Exit(self, **kwargs):
        pass

    @abstractmethod
    def Update(self, **kwargs):
        pass
