import GabesPythonToolBox.ControllSoftwere.StateMachine.BaseState as Base

class GoHomeState(Base.BaseState):
    def __init__(self, pointerTOScript=None):
        super().__init__(
            name="GoHomeState",
            canSwitchTo=["IdleState","SleepState"],
            pointerTOScript=pointerTOScript
        )
        #print("GoHomeState __init__")

    def Enter(self, **kwargs):
        print("Get path home")

    def Exit(self, **kwargs):
        print("Exiting GoHomeState")

    def Update(self, **kwargs):
        print("Moving Tword home")


