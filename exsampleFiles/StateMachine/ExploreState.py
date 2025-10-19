import GabesPythonToolBox.ControllSoftwere.StateMachine.BaseState as Base

class ExploreState(Base.BaseState):
    def __init__(self, pointerTOScript=None):
        super().__init__(
            name="ExploreState",
            canSwitchTO=["GoHomeState","IdleState"],  # list, not string
            pointerTOScript=pointerTOScript
        )
        print("ExploreState __init__")

    def Enter(self, **kwargs):
        print("Get plases to exsplore")

    def Exit(self, **kwargs):
        print("Exiting ExploreState")

    def Update(self, **kwargs):
        print("O a new fancy place to exsplore")


