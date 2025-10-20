# test_state_machine_dynamic.py

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
    manager = StateManager(stateFilePaths=state_files, defaultStateName="IdleState")

    # Log current state
    current_state = manager.state_switcher.GetCurrentStateName()
    Debug.log(f"Current State: {current_state}", LogType.Info, LogGroup.Showcase)

    # Call Update on default state
    manager.update()  

    # --- Test direct switches ---
    manager.state_switcher.SwitchState("ExploreState")
    manager.update()
    manager.state_switcher.SwitchState("GoHomeState")
    manager.update()
    manager.state_switcher.SwitchState("IdleState")
    manager.update()

    # --- Test manager pathfinding / request ---
    #one step
    success, path = manager.RequestState("GoHomeState")
    pretty_path = " -> ".join([p["state"] for p in path])
    Debug.log(f"Found a way to GoHomeState: {success}", LogType.Info, LogGroup.Showcase)
    Debug.log(f"Transition Path: {pretty_path}", LogType.Info, LogGroup.Showcase)

    #two step
    
    success, path = manager.RequestState("ExploreState")
    pretty_path = " -> ".join([p["state"] for p in path])
    Debug.log(f"Found a way to ExploreState: {success}", LogType.Info, LogGroup.Showcase)
    Debug.log(f"Transition Path: {pretty_path}", LogType.Info, LogGroup.Showcase)

    #three step
    
    success, path = manager.RequestState("SleepState")
    pretty_path = " -> ".join([p["state"] for p in path])
    Debug.log(f"Found a way to SleepState: {success}", LogType.Info, LogGroup.Showcase)
    Debug.log(f"Transition Path: {pretty_path}", LogType.Info, LogGroup.Showcase)

    #Zero step
    
    success, path = manager.RequestState("NoneState")
    pretty_path = " -> ".join([p["state"] for p in path])
    Debug.log(f"Found a way to NoneState: {success}", LogType.Info, LogGroup.Showcase)
    Debug.log(f"Transition Path: {pretty_path}", LogType.Info, LogGroup.Showcase)

    Debug.log(f"Curent state: {manager.state_switcher.GetCurrentStateName}", LogType.Info, LogGroup.Showcase) #shood not need to use state switcher at all


    Debug.log("State Machine Exsample Complete", "End", group="TEST")

if __name__ == "__main__":
    main()
