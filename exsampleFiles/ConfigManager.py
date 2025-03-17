from GabesPythonToolBox.Utility.Debug import Debug
#Debug.add_group('LIB', True) #Uncoment for the debug mesages

import GabesPythonToolBox.Utility.ConfigManager as CM

# Initialize the ConfigManager with the file path
config_manager = CM.startConfigManager("exsampleFiles\ConfigManager.json")

#Load and display the current configuration
config = config_manager()
print("Loaded Configuration:")
print(config)

# Update the player's name to "Opydian"
config_manager.update("player.name", "Opydian")
print("\nUpdated Player Name:", config_manager()["player"]["name"])

# Change the game difficulty to "hard"
config_manager.update("game_settings.difficulty", "hard")
print("\nUpdated Game Difficulty:", config_manager()["game_settings"]["difficulty"])

# Add a new item to the player's inventory
current_inventory = config_manager()["player"]["inventory"]
current_inventory.append("Dragon Scale")
config_manager.update("player.inventory", current_inventory)
print("\nUpdated Inventory:", config_manager()["player"]["inventory"])

# Update the progress of the first quest (Defeat the Dragon)
config_manager.update("quests.active[0].progress", 80)
print("\nUpdated Quest Progress (Defeat the Dragon):", config_manager()["quests"]["active"][0]["progress"])

# Save the updated configuration back to the Newfile
config_manager.save("exsampleFiles\ConfigManager2.json")
print("\nnew file saved:")
print(config_manager())

# Reset the configuration to the default configuration
config_manager.reset()  # No arguments needed because it uses the default config saved when the object is initialized
print("\nConfiguration Reset:")
print(config_manager())

# Save the updated configuration back to the file
config_manager.save("exsampleFiles\ConfigManager.json")
print("\nConfiguration has been saved back to the file.")


# Initialize the ConfigManager with another configuration to add to the current one
add_config_manager = CM.startConfigManager("exsampleFiles\ConfigManager3.json")

# Load and display the configuration that will be added
add_config = add_config_manager()
print("\nLoaded Configuration to Add:")
print(add_config)

# Add the new configuration to the current configuration
# Assuming the `add()` method uses `self.config.update(new_config)` to merge the configurations
config_manager.add(add_config)
print("\nConfiguration After Adding New Data:")
print(config_manager())

# Save the updated configuration to a new file after the addition
config_manager.save("exsampleFiles\ConfigManager4.json")
print("\nNew file saved after addition:")
print(config_manager())