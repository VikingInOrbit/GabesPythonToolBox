from GabesPythonToolBox.ControllSoftwere.StateMachine.StateManager import StateManager
from GabesPythonToolBox.Utility.Debug import Debug, LogType, LogGroup

state_files = [
    r"exsampleFiles/StateMachine/ExploreState.py",
    r"exsampleFiles/StateMachine/GoHomeState.py",
    r"exsampleFiles/StateMachine/IdleState.py",
    r"exsampleFiles/StateMachine/SleepState.py",
    r"exsampleFiles/StateMachine/NoneState.py"
]

def main():
    Debug.log("Starting Dynamic State Machine Test", "Header", group="TEST")

    # Initialize StateManager with default state "IdleState"
    SM = StateManager(stateFilePaths=state_files, defaultStateName="IdleState")

    # Log current state
    current_state = SM.state_switcher.GetCurrentStateName()
    Debug.log(f"Current State: {current_state}", LogType.Info, LogGroup.Showcase)

    # Call Update on default state
    SM.update()  

    # --- Test direct switches ---
    SM.RequestState("ExploreState",Teleport=True)
    SM.update()
    SM.RequestState("GoHomeState",Teleport=True)
    SM.update()
    SM.RequestState("IdleState",Teleport=True)
    SM.update()

    #Teleport=telep
    SM.RequestDefaultState()
    

    # --- Test manager pathfinding / request ---
    #one step
    success, path = SM.RequestState("GoHomeState")
    pretty_path = " -> ".join([p["state"] for p in path])
    Debug.log(f"Found a way to GoHomeState: {success}", LogType.Info, LogGroup.Showcase)
    Debug.log(f"Transition Path: {pretty_path}", LogType.Info, LogGroup.Showcase)

    #two step
    
    success, path = SM.RequestState("ExploreState")
    pretty_path = " -> ".join([p["state"] for p in path])
    Debug.log(f"Found a way to ExploreState: {success}", LogType.Info, LogGroup.Showcase)
    Debug.log(f"Transition Path: {pretty_path}", LogType.Info, LogGroup.Showcase)

    #three step
    
    success, path = SM.RequestState("SleepState")
    pretty_path = " -> ".join([p["state"] for p in path])
    Debug.log(f"Found a way to SleepState: {success}", LogType.Info, LogGroup.Showcase)
    Debug.log(f"Transition Path: {pretty_path}", LogType.Info, LogGroup.Showcase)

    #Zero step
    
    success, path = SM.RequestState("NoneState")
    pretty_path = " -> ".join([p["state"] for p in path])
    Debug.log(f"Found a way to NoneState: {success}", LogType.Info, LogGroup.Showcase)
    Debug.log(f"Transition Path: {pretty_path}", LogType.Info, LogGroup.Showcase)

    Debug.log(f"Curent state: {SM.GetCurrentStateName()}", LogType.Info, LogGroup.Showcase) 

    Debug.log(f"DefaultState: {SM.GetDefaultStateName()}", LogType.Info, LogGroup.Showcase) 

    SM.RequestDefaultState(Teleport=True)

    Debug.log(f"Curent state: {SM.GetCurrentStateName()}", LogType.Info, LogGroup.Showcase) 


    Debug.log("State Machine Exsample Complete", "End", group="TEST")

if __name__ == "__main__":
    main()
