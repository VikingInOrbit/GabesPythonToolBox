from GabesPythonToolBox.ControllSoftwere.StateMachine.StateManager import StateManager
from GabesPythonToolBox.Utility.Debug import *

# List of state files to load
state_files = [
    r"exsampleFiles/StateMachine/ExploreState.py",
    r"exsampleFiles/StateMachine/GoHomeState.py",
    r"exsampleFiles/StateMachine/IdleState.py",
    r"exsampleFiles/StateMachine/SleepState.py",
    r"exsampleFiles/StateMachine/NoneTestState.py"
]

def main():
    Debug.log("Starting Dynamic State Machine Test", "Header", group="TEST")

    # Initialize StateManager with default state "IdleState"
    SM = StateManager(stateFilePaths=state_files, defaultStateName="IdleState")
    SM.RequestDefaultState(Teleport=True)

    # Log current state
    Debug.log(f"Current State: {SM.GetCurrentStateName()}", LogType.Info, LogGroup.Showcase)

    # --- Call Update on default state ---
    Debug.log("Updating default state...", LogType.Info, LogGroup.Showcase)
    SM.update()  

    # --- Test direct switches with Teleport ---
    Debug.log("", LogType.NoneType, LogGroup.Showcase)
    Debug.log("Testing direct switches with Teleport", LogType.Info, LogGroup.Showcase)
    for target in ["ExploreState", "GoHomeState", "IdleState", "ExploreState"]:
        SM.RequestState(target, Teleport=True)
        SM.update()

    # --- Test returning to default state ---
    Debug.log("", LogType.NoneType, LogGroup.Showcase)
    Debug.log("Requesting default state", LogType.Info, LogGroup.Showcase)
    Debug.log(f"Default state: {SM.GetDefaultStateName()}, Current state: {SM.GetCurrentStateName()}", LogType.Info, LogGroup.Showcase)
    SM.RequestDefaultState()
    Debug.log(f"New Current state: {SM.GetCurrentStateName()}", LogType.Info, LogGroup.Showcase)

    # --- Test manager pathfinding / multi-step transitions ---
    Debug.log("", LogType.NoneType, LogGroup.Showcase)
    Debug.log("Testing pathfinding requests", LogType.Info, LogGroup.Showcase)
    for target in ["GoHomeState", "ExploreState", "SleepState", "NoneTestState"]:
        success, path = SM.RequestState(target)
        if path:
            pretty_path = " -> ".join([p["state"] for p in path])
        else:
            pretty_path = "No path found"
        Debug.log(f"Target: {target}, Success: {success}", LogType.Info, LogGroup.Showcase)
        Debug.log(f"Transition Path: {pretty_path}", LogType.Info, LogGroup.Showcase)

    # --- Log current and default states ---
    Debug.log("", LogType.NoneType, LogGroup.Showcase)
    Debug.log(f"Current State: {SM.GetCurrentStateName()}", LogType.Info, LogGroup.Showcase)
    Debug.log(f"Default State: {SM.GetDefaultStateName()}", LogType.Info, LogGroup.Showcase)

    # --- Return to default state again ---
    Debug.log("Returning to default state with Teleport", LogType.Info, LogGroup.Showcase)
    SM.RequestDefaultState(Teleport=True)
    Debug.log(f"Current State: {SM.GetCurrentStateName()}", LogType.Info, LogGroup.Showcase)

    Debug.log("State Machine Example Complete", "End", group="TEST")


if __name__ == "__main__":
    main()
