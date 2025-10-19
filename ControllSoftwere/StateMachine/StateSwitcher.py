from ...Utility import ConfigManager as CM
from ...Utility.Debug import *

class StateMachine:
    def __init__(self, defaultStateName):
        Debug.log("StateMachine init", "Header", group="LIB")
        self.defaultStateName = defaultStateName
        self.State = None
        self.States = {}  # store by name
        Debug.log("StateMachine init", "End", group="LIB")

    def __call__(self, **kwargs):
        # call current state's Update
        if self.State:
            self.State(**kwargs)

    def AddState(self, state, setDefault=False):
        self.States[state.name] = state
        if setDefault or self.State is None:
            self.State = state
            self.State.Enter()

    def RemoveState(self, stateName):
        if stateName in self.States:
            del self.States[stateName]

    def SwitchState(self, stateName):
        if stateName in self.States and stateName != self.State.name:
            if stateName not in self.State.canSwitchTo:
                Debug.log(f"Cannot switch from {self.State.name} to {stateName}, can switch to {self.State.canSwitchTo}", LogType.Warning ,LogGroup.WarningError)
            self.State = self.States[stateName]
            self.State.Enter()

    def DefaultState(self):
        if self.defaultStateName in self.States:
            self.SwitchState(self.defaultStateName)
    
    def GetStatesCanSwitchTo(self):
        if self.State is None:
            return []
        return self.State.canSwitchTo


def StartStateManager(filePath) -> StateMachine:
    Debug.log("Start State Manager", "Header", group="LIB")
    
    # Load state config from file (placeholder)
    states = None #StateFactory()  # returns list of State objects
    
    default_state_name = states[0].name if states else None
    sm = StateMachine(default_state_name)

    for state in states:
        sm.AddState(state, setDefault=(state.name==default_state_name))

    Debug.log("Start State Manager", "End", group="LIB")
    return sm


