import json
import os
import copy
from ..Utility.Debug import *

class ConfigManager:
    """
    A utility class to manage JSON configuration files.
    """

    def __init__(self, configFilePath: str = None):
        """
        Initialize the ConfigManager.

        :param configFilePath: (str) Path to the JSON configuration file.
        """
        Debug.log(f"ConfigManager init","Header",group="LIB")
        Debug.log(f"config File Path: {configFilePath}","Info",group="LIB")
        Debug.log(f"ConfigManager init","End",group="LIB")
        self.loadConfig(configFilePath)

    def __call__(self):
        """
        Get the configuration file.

        :return: (dict) The current configuration data.
        """
        Debug.log(f"ConfigManager call","Header",group="LIB")
        
        if self.config:
            Debug.log(f"ConfigManager call","End",group="LIB")
            return self.config
        else:
            Debug.log("no Config Loaded","Info",group="LIB")
            Debug.log(f"ConfigManager call","End",group="LIB")

    def loadConfig(self, configFilePath: str = None):
        """
        Load and parse the JSON configuration file.

        :return: (dict) Parsed configuration data.
        :raises FileNotFoundError: If the file does not exist.
        :raises ValueError: If the file contains invalid JSON.
        """
        Debug.log(f"loadConfig","Header",group="LIB")
        
        
        if not os.path.exists(configFilePath):
            Debug.log(f"loadConfig","End",group="LIB")
            raise FileNotFoundError(f"Configuration file {configFilePath} not found.")
        
        with open(configFilePath, 'r') as file:
            try:
                self.config = json.load(file)
                self.defaultConfig = copy.deepcopy(self.config)  # Create a deep copy
                Debug.log(f"loaded config","Info",group="LIB")
            except json.JSONDecodeError:
                Debug.log(f"loadConfig","End",group="LIB")
                raise ValueError(f"Failed to decode JSON in {configFilePath}.")
            
        Debug.log(f"loadConfig","End",group="LIB")

    def update(self, key, value):
        """ 
        Update a specific configuration value using dot notation for nested keys.
    
        :param key: (str) Key to update (e.g., 'robot_legs.leg_1.joints[0].pid.kp').
        :param value: New value to set.
        :raises KeyError: If the key does not exist in the configuration.
        """
        Debug.log(f"ConfigManager update","Header",group="LIB")
        
        keys = key.split('.')
        config_section = self.config

        for i, k in enumerate(keys[:-1]):
            # Detect array indices in keys (e.g., 'active[0]')
            if "[" in k and "]" in k:
                array_key, index = k[:-1].split("[")
                config_section = config_section[array_key][int(index)]
            else:
                k = int(k) if k.isdigit() else k  # Convert to integer for list indices
                config_section = config_section[k]

            # Handle the final key
            final_key = keys[-1]
            if "[" in final_key and "]" in final_key:
                array_key, index = final_key[:-1].split("[")
                config_section[array_key][int(index)] = value
            else:
                final_key = int(final_key) if final_key.isdigit() else final_key
                config_section[final_key] = value

        Debug.log(f"ConfigManager update","End",group="LIB")

    def add(self, data):
        """
        Add a new data set to the current configuration.
        This method will add a new dictionary (data) to the existing configuration.
    
        :param data: (dict) The new configuration data to be appended.
        """
        Debug.log(f"ConfigManager add", "Header", group="LIB")

        if isinstance(data, dict):
            # Check if the data is a dictionary before appending
            self.config.update(data)  # Append the new data to the existing configuration
            Debug.log(f"Add new data", "Info", group="LIB")
        else:
            # Handle the case where data is not a dictionary
            Debug.log(f"Invalid data format. Expected dict, got {type(data)}", "Error", group="LIB")

        Debug.log(f"ConfigManager add", "End", group="LIB")


    def reset(self):
        """
        Reset the configuration to a default state.

        :param defaultConfig: (dict) The default configuration to reset to.
        """
        self.config = self.defaultConfig
        
    def save(self,configFilePath: str = None):
        """
        Save the current configuration to a file.
        """

        Debug.log(f"ConfigManager save","Header",group="LIB")

        if not configFilePath:
            Debug.log(f"no fIle Path given","Info",group="LIB")
            Debug.log(f"ConfigManager save","End",group="LIB")
            return

        with open(configFilePath, 'w') as file:
            json.dump(self.config, file, indent=4)
            Debug.log(f"Save","Info",group="LIB")

        Debug.log(f"ConfigManager save","End",group="LIB")
    
def startConfigManager(configFilePath: str = None):
    """
    Create and return a ConfigManager instance.

    :param configFilePath: (str) Path to the JSON configuration file.
    :return: (ConfigManager) An instance of the ConfigManager.
    """
    Debug.log(f"start ConfigManager","Header",group="LIB")
    Debug.log(f"start ConfigManager","End",group="LIB")
    return ConfigManager(configFilePath)
