from abc import ABC, abstractmethod
from ...Utility.Debug import *

class BaseState(ABC):
    def __init__(self, name, canSwitchTo=None, **kwargs):
        Debug.log("BaseState __init__", "Header", group="LIB")
        self.name = name
        self.canSwitchTo = canSwitchTo or []
        self.metadata = kwargs  # store any extra parameters
        Debug.log(f"BaseState '{self.name}' initialized with canSwitchTo={self.canSwitchTo}", LogType.Info, LogGroup.LIB)
        Debug.log("BaseState __init__", "End", group="LIB")

    def __call__(self, **kwargs):
        """Allow state() to trigger an update."""
        Debug.log("BaseState __call__", "Header", group="LIB")
        
        self.Update(**kwargs)
        Debug.log("BaseState __call__", "End", group="LIB")

    @abstractmethod
    def Enter(self, **kwargs):
        """Called when state becomes active."""
        pass

    @abstractmethod
    def Exit(self, **kwargs):
        """Called when state is exited."""
        pass

    @abstractmethod
    def Update(self, **kwargs):
        """Called by state machine."""
        pass

    def AddSwitchableState(self, state_name):
        if state_name not in self.canSwitchTo:
            self.canSwitchTo.append(state_name)

    def RemoveSwitchableState(self, state_name):
        if state_name in self.canSwitchTo:
            self.canSwitchTo.remove(state_name)

    def GetSwitchableStates(self):
        return self.canSwitchTo

    def SetSwitchableStates(self, states_list):
        self.canSwitchTo = states_list
