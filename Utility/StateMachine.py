from ..Utility import ConfigManager as CM

from typing import Any

#shood be able to switch between states and have "start,exsit,update"

class StateMachine:
    def __init__(self, defoultState):
        self.defoultState = defoultState
        self.State = None
        self.States[] = None

    def __call__(self):
        return self.State

    def AddState(State, setDefoultState = False) -> None:
        ...

    def RemoveState() -> None:
        ...

    def SwitchState() -> None:
        ...

    def DefoultState() -> None:
        #
        ...

class State:
    def __init__(self,name,canSwitchTO,pointerTOScript) -> None:
        self.canSwitchTO [None] #list

        def start():
            #pointerTOScript.start
            ...

        def exsit():
            #pointerTOScript.start
            ...

        def update():
            #pointerTOScript.start
            ...

def StartStateManager(FilePath):
    #inisialise state manager ith config file
    ...