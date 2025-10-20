import GabesPythonToolBox.ControllSoftwere.StateMachine.BaseState as Base

class SleepState(Base.BaseState):
    def __init__(self, pointerTOScript=None):
        super().__init__(
            name="SleepState",
            canSwitchTo=["GoHomeState"],  # list, not string
            pointerTOScript=pointerTOScript
        )
        #print("SleepState __init__")

    def Enter(self, **kwargs):
        print("Setting movement to 0, turning off")

    def Exit(self, **kwargs):
        print("Is it morning already?")

    def Update(self, **kwargs):
        print("Im sleeping")


