import GabesPythonToolBox.ControllSoftwere.StateMachine.BaseState as Base

class GoHomeState(Base.BaseState):
    def __init__(self, pointerTOScript=None):
        super().__init__(
            name="GoHomeState",
            canSwitchTO=["ExploreState","IdleState"],
            pointerTOScript=pointerTOScript
        )
        print("GoHomeState __init__")

    def Enter(self, **kwargs):
        print("Get path home")

    def Exit(self, **kwargs):
        print("Exiting GoHomeState")

    def Update(self, **kwargs):
        print("Moving Tword home")


