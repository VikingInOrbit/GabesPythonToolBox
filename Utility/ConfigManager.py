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
