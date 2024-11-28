
import json
import os

class ConfigManager:
    def __init__(self, configFilePath):
        self.configFilePath = configFilePath #add reative file path suport
        self.config = self.reedConfig()

    def __call__(self):
        return self.reedConfig()
    
    def reedConfig(self):
        if not os.path.exists(self.configFilePath):
            raise FileNotFoundError(f"Configuration file {self.configFilePath} not found.")
        
        with open(self.configFilePath, 'r') as file:
            try:
                config= json.load(file)
            except json.JSONDecodeError:
                raise ValueError(f"Failed to decode JSON in {self.configFilePath}.")
        
        return config
    
    def updateConfig(self):
        #update config
        return
    
def startConfigManager(filePath):
    #chek file path
    return ConfigManager(filePath)