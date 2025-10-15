import GabesPythonToolBox.ControllSoftwere.StateMachine.BaseState as Base

class IdleState(Base.BaseState):
    def __init__(self, pointerTOScript=None):
        super().__init__(
            name="IdleState",
            canSwitchTO=["GoHomeState","ExploreState"],  # list, not string
            pointerTOScript=pointerTOScript
        )
        print("IdleState __init__")

    def Enter(self, **kwargs):
        print("Setting movement to 0")

    def Exit(self, **kwargs):
        print("Exiting IdleState")

    def Update(self, **kwargs):
        print("Ensuring we are standing still")


