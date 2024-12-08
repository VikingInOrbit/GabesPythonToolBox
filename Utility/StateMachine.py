from ..Utility import ConfigManager as CM
from ..Utility.Debug import *

from typing import Any

#shood be able to switch between states and have "start,exsit,update"

class StateMachine: # realay on update timing outside of lib
    def __init__(self, defoultState):
        Debug.log(f"StateMachine init","Header",group="LIB")
        self.defoultState = defoultState
        self.State = None
        self.States = []
        Debug.log(f"StateMachine init","End",group="LIB")

    def __call__(self):
        Debug.log(f"StateMachine call","Header",group="LIB")
        Debug.log(f"StateMachine call","End",group="LIB")
         #update state

    def AddState(State, setDefoultState = False) -> None:
        Debug.log(f"Add State","Header",group="LIB")
        Debug.log(f"Add State","End",group="LIB")
        

    def RemoveState() -> None:
        Debug.log(f"Remove State","Header",group="LIB")
        Debug.log(f"Remove State","End",group="LIB")
        

    def SwitchState() -> None:
        Debug.log(f"Switch State","Header",group="LIB")
        Debug.log(f"Switch State","End",group="LIB")
        

    def DefoultState() -> None:
        Debug.log(f"Defoult State","Header",group="LIB")
        Debug.log(f"Defoult State","End",group="LIB")

class State:
    def __init__(self,name,canSwitchTO,pointerTOScript) -> None:
        self.canSwitchTO = canSwitchTO #list
        self.name = name
        Debug.log(f"State {self.name} init","Header",group="LIB")
        Debug.log(f"State {self.name} init","End",group="LIB")

             
        def Enter() -> None:
            Debug.log(f"State {self.name} Enter","Header",group="LIB")
            Debug.log(f"State {self.name} Enter","End",group="LIB")
            #pointerTOScript.start
            

        def Exsit() -> None:
            Debug.log(f"State {self.name} Exsit","Header",group="LIB")
            Debug.log(f"State {self.name} Exsit","End",group="LIB")
            #pointerTOScript.start
            

        def Update() -> None:
            Debug.log(f"State {self.name} Update","Header",group="LIB")
            Debug.log(f"State {self.name} Update","End",group="LIB")
            #pointerTOScript.start
            

def StartStateManager(FilePath)  -> StateMachine:
    Debug.log(f"Start State Manager","Header",group="LIB")
    Debug.log(f"Start State Manager","End",group="LIB")
    #inisialise state manager ith config file
    

def StateFactory()-> State:
    Debug.log(f"State Factory","Header",group="LIB")
    Debug.log(f"State Factory","End",group="LIB")