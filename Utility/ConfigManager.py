import json
import os
import copy

class ConfigManager:
    """
    A utility class to manage JSON configuration files.
    """

    def __init__(self, configFilePath):
        """
        Initialize the ConfigManager.

        :param configFilePath: (str) Path to the JSON configuration file.
        """
        self.configFilePath = os.path.abspath(configFilePath)
        self.config = self._loadConfig()
        self.defaultConfig = copy.deepcopy(self.config)  # Create a deep copy

    def __call__(self):
        """
        Reload the configuration file.

        :return: (dict) The current configuration data.
        """
        return self.config

    def _loadConfig(self):
        """
        Load and parse the JSON configuration file.

        :return: (dict) Parsed configuration data.
        :raises FileNotFoundError: If the file does not exist.
        :raises ValueError: If the file contains invalid JSON.
        """
        if not os.path.exists(self.configFilePath):
            raise FileNotFoundError(f"Configuration file {self.configFilePath} not found.")
        
        with open(self.configFilePath, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                raise ValueError(f"Failed to decode JSON in {self.configFilePath}.")

    def update(self, key, value):
        """ 
        Update a specific configuration value using dot notation for nested keys.
    
        :param key: (str) Key to update (e.g., 'robot_legs.leg_1.joints[0].pid.kp').
        :param value: New value to set.
        :raises KeyError: If the key does not exist in the configuration.
        """
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


    def reset(self):
        """
        Reset the configuration to a default state.

        :param defaultConfig: (dict) The default configuration to reset to.
        """
        self.config = self.defaultConfig
        
    def save(self):
        """
        Save the current configuration back to the file.
        """
        with open(self.configFilePath, 'w') as file:
            json.dump(self.config, file, indent=4)
    
    def saveNew(self,FileName):
        """
        Save the current configuration back to the file.
        """
        with open(os.path.abspath(FileName), 'w') as file:
            json.dump(self.config, file, indent=4)


def startConfigManager(configFilePath):
    """
    Create and return a ConfigManager instance.

    :param configFilePath: (str) Path to the JSON configuration file.
    :return: (ConfigManager) An instance of the ConfigManager.
    """
    return ConfigManager(configFilePath)
