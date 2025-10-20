import importlib.util
import inspect
import sys
from .BaseState import BaseState
from ...Utility.Debug import Debug, LogType, LogGroup
import os

class StateLoader:
    def __init__(self, state_file_paths=None):
        """
        :param state_file_paths: List of relative paths to state files (e.g., ["States/IdleState.py"])
        """
        self.state_file_paths = state_file_paths or []
        self.loaded_modules = {}
        self.loaded_states = {}

    def LoadStates(self):
        """Dynamically loads state classes from the given list of file paths."""
        Debug.log("StateLoader: loading states from file list...", "Header", group="LIB")

        for file_path in self.state_file_paths:
            if not os.path.exists(file_path):
                Debug.log(f"State file not found: {file_path}", LogType.Warning, LogGroup.WarningError)
                continue

            module_name = os.path.splitext(os.path.basename(file_path))[0]

            try:
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                self.loaded_modules[module_name] = module

                # Discover classes that subclass BaseState
                for obj in module.__dict__.values():
                    if inspect.isclass(obj) and issubclass(obj, BaseState) and obj is not BaseState:
                        instance = obj()
                        self.loaded_states[instance.name] = instance
                        Debug.log(f"Loaded state: {instance.name} from {file_path}", "Info", group="LIB")

            except Exception as e:
                Debug.log(f"Failed to load {file_path}: {e}", LogType.Warning, LogGroup.WarningError)

        Debug.log("StateLoader: all specified states loaded.", "End", group="LIB")
        return self.loaded_states

    def UnloadState(self, state_name):
        """Unload a specific state from memory."""
        state = self.loaded_states.pop(state_name, None)
        if not state:
            return
        # Remove module reference
        for mod_name, mod in list(self.loaded_modules.items()):
            if state_name.lower() in mod_name.lower():
                del sys.modules[mod_name]
                del self.loaded_modules[mod_name]
                Debug.log(f"Unloaded state: {state_name}", "Info", group="LIB")

    def GetLoadedStates(self):
        return self.loaded_states
