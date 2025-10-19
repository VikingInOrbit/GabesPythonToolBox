# test_state_machine.py

import GabesPythonToolBox.ControllSoftwere.StateMachine.StateSwitcher as SM


import IdleState 
import GoHomeState
import ExploreState

# --- Build and test the State Machine ---
def main():
    # Create the State Machine with default state name "IdleState"
    sm = SM.StateMachine(defaultStateName="IdleState")

    # Create state objects
    idle = IdleState.IdleState()
    gohome = GoHomeState.GoHomeState()
    explore = ExploreState.ExploreState()

    # Add states
    sm.AddState(idle, setDefault=True)
    sm.AddState(gohome)
    sm.AddState(explore)

    print()

    print("State Machine Test")

    # Run default (Idle)
    sm()  

    sm.SwitchState("ExploreState")
    sm()  
    sm()  
    sm()  

    sm.SwitchState("GoHomeState")
    sm()

    sm.SwitchState("IdleState")
    sm() 


if __name__ == "__main__":
    main()
