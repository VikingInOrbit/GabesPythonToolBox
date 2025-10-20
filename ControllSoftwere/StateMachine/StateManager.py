from ...Utility.Debug import Debug, LogType, LogGroup

from ...ControllSoftwere.StateMachine.StateLoader import StateLoader
from ...ControllSoftwere.StateMachine.StateSwitcher import StateSwitcher

from collections import deque

class StateManager:
    def __init__(self, stateFilePaths,defaultStateName):

        loader = StateLoader(state_file_paths=stateFilePaths)
        startStates = loader.LoadStates()

        self.state_switcher = StateSwitcher(startStates, default_state_name=defaultStateName)

    def RequestState(self, target_state_name,Teleport:bool=False): #TODO teleport means dont find a path just switch
        """Try to move to a target state. Returns (success, path)."""
        current_name = self.GetCurrentStateName()
        if not current_name:
            Debug.log("No current state. Forcing switch.", LogType.Warning, LogGroup.WarningError)
            self.state_switcher.SwitchState(target_state_name)
            return True, [{"state": target_state_name, "current": True}]

        if target_state_name == current_name:
            Debug.log(f"Already in {target_state_name}", "Info", group="LIB")
            return True, [{"state": target_state_name, "current": True}]
        
        if Teleport:
            Debug.log(f"Teleported from: {current_name} to target_state_name", LogType.Info, LogGroup.LIB)
            self.state_switcher.SwitchState(target_state_name)
            return True, [{"state": target_state_name, "current": True}]

        # BFS to find a valid path from current to target
        path = self._find_path(current_name, target_state_name)
        if not path:
            Debug.log(f"No valid path from {current_name} to {target_state_name}", LogType.Warning, LogGroup.WarningError)
            return False, []

        Debug.log(f"Transition path: {path}", "Info", group="LIB")

        # Execute the path (skipping the first one since it’s the current)
        for next_state in path[1:]:
            self.state_switcher.SwitchState(next_state)

        # Build structured path result
        result = [{"state": s} for s in path]
        return True, result

    def _find_path(self, start, goal):
        """Breadth-first search through canSwitchTo relationships."""
        states = self.state_switcher.States
        if start not in states or goal not in states:
            return None

        visited = set()
        queue = deque([[start]])

        while queue:
            path = queue.popleft()
            current = path[-1]
            if current == goal:
                return path
            visited.add(current)

            for next_state in states[current].canSwitchTo:
                if next_state not in visited and next_state in states:
                    queue.append(path + [next_state])
        return None

    def update(self,**kwargs):
        self.state_switcher(**kwargs)

    def RequestDefaultState(self,Teleport:bool=False):
        if Teleport:
            self.state_switcher.DefaultState()
            return
        
        target_state_name = self.GetCurrentStateName()
        self.RequestState(target_state_name)

    def GetCurrentStateName(self):
        return self.state_switcher.GetCurrentStateName()
    
    def GetDefaultStateName(self):
        return self.state_switcher.GetDefaultStateName()