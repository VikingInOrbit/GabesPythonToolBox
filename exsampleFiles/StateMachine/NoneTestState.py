import GabesPythonToolBox.ControllSoftwere.StateMachine.BaseState as Base

class NoneState(Base.BaseState):
    def __init__(self, pointerTOScript=None):
        super().__init__(
            name="NoneState",
            canSwitchTo=[],  # list, not string
            pointerTOScript=pointerTOScript
        )
        #print("NoneState __init__")

    def Enter(self, **kwargs):
        print("How Did you get here?")

    def Exit(self, **kwargs):
        print("Good readence")

    def Update(self, **kwargs):
        print("Im still not here")


