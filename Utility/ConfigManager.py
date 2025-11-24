import json
import yaml
import os
import copy
from ..Utility.Debug import *
from ..DataProsesing.DataRW import *

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
 
        self.config = None
        self.defaultConfig = None

        if not configFilePath:
            Debug.log(f"No fIle Path given","Warning",group="WarningError")
            Debug.log(f"ConfigManager init","End",group="LIB")
            return
        
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

    def loadConfig(self, configFilePath: str = None): # TODO how do i deal with / and \ in the file name?
        """
        Load and parse the JSON configuration file.

        :return: (dict) Parsed configuration data.
        :raises FileNotFoundError: If the file does not exist.
        :raises ValueError: If the file contains invalid JSON.
        """
        Debug.log(f"loadConfig","Header",group="LIB")
        
        if not os.path.exists(configFilePath):
            Debug.log(f"loadConfig","End",group="LIB")
            raise FileNotFoundError(f"Configuration file {configFilePath} not found.") #TODO dues not print right
        

        fileType = None

        ext = os.path.splitext(configFilePath)[1].lower()
        if ext not in (".json", ".yaml", ".yml"):
            raise ValueError(f"Unsupported config file type: {ext}")


        self.config = read_data(configFilePath)
        
        self.defaultConfig = copy.deepcopy(self.config)  # Create a deep copy
        Debug.log(f"loaded config: \n{self.config}","Info",group="LIB")

        Debug.log(f"loadConfig","End",group="LIB")

    def update(self, key, value):
        """ 
        Update a specific configuration value using dot notation for nested keys.
    
        :param key: (str) Key to update (e.g., 'robot_legs.leg_1.joints[0].pid.kp').
        :param value: New value to set.
        :raises Exception: If the key path does not exist or types do not match.
        """
        Debug.log(f"ConfigManager update","Header",group="LIB")
        
        if self.config is None:
            raise Exception("No configuration loaded to update.")

        keys = key.split('.')
        config_section = self.config

        try:
            # Traverse to the parent of the final key
            for k in keys[:-1]:
                if "[" in k and k.endswith("]"):
                    array_key, index = k[:-1].split("[")
                    array_key = int(array_key) if str(array_key).isdigit() else array_key
                    config_section = config_section[array_key][int(index)]
                else:
                    k_idx = int(k) if str(k).isdigit() else k
                    config_section = config_section[k_idx]


            final_key = keys[-1]
            if "[" in final_key and final_key.endswith("]"):
                array_key, index = final_key[:-1].split("[")
                array_key = int(array_key) if str(array_key).isdigit() else array_key
                config_section[array_key][int(index)] = value
            else:
                final_key_idx = int(final_key) if str(final_key).isdigit() else final_key
                config_section[final_key_idx] = value

        except (KeyError, IndexError, TypeError) as e:
            raise Exception(f"Failed to update key '{key}': {e}")

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
        
    def save(self,configFilePath: str = None,fileType:str=""):
        """
        Save the current configuration to a file.
        """

        Debug.log(f"ConfigManager save","Header",group="LIB")

        if os.path.splitext(configFilePath)[1].lower():
            Debug.log(f"File exstension found using that","Info",group="LIB")
            fileType = os.path.splitext(configFilePath)[1].lower()
            Debug.log(f"File exstension found: {fileType}","Info",group="LIB")

        if not configFilePath:
            Debug.log(f"No fIle Path given","Warning",group="WarningError")
            Debug.log(f"ConfigManager save","End",group="LIB")
            return

        Debug.log(f"Saveing config: \n {self.config}","Info",group="LIB")

        write_data(configFilePath,self.config)

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
