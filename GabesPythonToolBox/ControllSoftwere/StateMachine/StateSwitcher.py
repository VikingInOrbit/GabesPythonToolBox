from ...ControllSoftwere.StateMachine.NoneState import NoneState
from ...Utility import ConfigManager as CM
from ...Utility.Debug import *


class StateSwitcher:
    def __init__(self, startStates, default_state_name: str = None):
        Debug.log("StateSwitcher init", "Header", group="LIB")
        NoneState_ = NoneState()

        self.default_state_name = default_state_name
        self.State = NoneState_
        self.States = {}  # Dictionary: {state_name: state_instance}

        for addState in startStates.values():  # TODO flytt dette inn i manager
            self.AddState(addState, setDefault=(addState.name == default_state_name))
        Debug.log("StateSwitcher init", "End", group="LIB")

    def __call__(self, **kwargs):
        """Forward call to the current state's Update."""
        if self.State:
            self.State(**kwargs)

    def AddState(self, state, setDefault=False):
        """Register a state instance."""
        self.States[state.name] = state
        if setDefault or self.default_state_name is None:
            self.default_state_name = state.name

    def RemoveState(self, state_name):
        """Remove state from registry."""
        if state_name in self.States:
            del self.States[state_name]

    def SwitchState(
        self, state_name
    ):  # TODO make it a syncronus so the enter/exsit can hapon
        """Switch between loaded states. Will perform illegal switches but logs a warning."""
        if state_name not in self.States:
            Debug.log(
                f"State {state_name} not found.", LogType.Warning, LogGroup.WarningError
            )
            return

        if not self.State:
            Debug.log(
                "No current state. Forcing direct switch.",
                LogType.Warning,
                LogGroup.WarningError,
            )
            self.State = self.States[state_name]
            self.State.Enter()
            return

        if state_name == self.State.name:
            Debug.log(f"Already in state {state_name}.", LogType.Info, LogGroup.LIB)
            return

        if state_name not in self.State.canSwitchTo:
            Debug.log(
                f"Illegal transition: {self.State.name} : {state_name}. "
                f"Allowed: {self.State.canSwitchTo}",
                LogType.Warning,
                LogGroup.WarningError,
            )

        # Perform the switch anyway
        self.State.Exit()
        self.State = self.States[state_name]
        self.State.Enter()

    def DefaultState(self):
        """Switch to default state if it exists."""
        if self.default_state_name:
            self.SwitchState(self.default_state_name)

    def GetCurrentStateName(self):
        return self.State.name if self.State else None

    def GetDefaultStateName(self):
        return self.default_state_name

    def GetStatesCanSwitchTo(self):
        """Returns allowed transitions from current state."""
        return self.State.canSwitchTo if self.State else []
