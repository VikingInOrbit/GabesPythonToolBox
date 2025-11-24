import GabesPythonToolBox.ControllSoftwere.StateMachine.BaseState as Base

from ...Utility.Debug import *


class NoneState(Base.BaseState):
    def __init__(self, pointerTOScript=None):
        super().__init__(
            name="NoneState",
            canSwitchTo=[],  # list, not string
            pointerTOScript=pointerTOScript,
        )
        # print("NoneState __init__")

    def Enter(self, **kwargs):
        pass

    def Exit(self, **kwargs):
        pass

    def Update(self, **kwargs):
        Debug.log(f"Called NoneState.", LogType.Info, LogGroup.LIB)
        pass
