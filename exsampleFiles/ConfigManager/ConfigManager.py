from GabesPythonToolBox.Utility.Debug import Debug
Debug.add_group('Showcase', True)
#TODO Debug 

import GabesPythonToolBox.Utility.ConfigManager as CM


Debug.log("ConfigManager Showcase", message_type="Header", group="Showcase")
Debug.log("", message_type="None", group="Showcase")



# Initialize the ConfigManager with the file path
config_manager = CM.startConfigManager("exsampleFiles/ConfigManager/ConfigManager.json")

#Load and display the current configuration
config = config_manager()
Debug.log("Loaded Configuration:", message_type="Info", group="Showcase")
Debug.log(config, message_type="Info", group="Showcase")
Debug.log("", message_type="None", group="Showcase")

# Update the player's name to "Opydian"
config_manager.update("player.name", "Opydian")
Debug.log(f"Updated Player Name: {config_manager()['player']['name']}", message_type="Info", group="Showcase")


# Change the game difficulty to "hard"
config_manager.update("game_settings.difficulty", "hard")
Debug.log(f"Updated Game Difficulty: {config_manager()['game_settings']['difficulty']}", message_type="Info", group="Showcase")
Debug.log("", message_type="None", group="Showcase")


# Add a new item to the player's inventory
Debug.log(f"Current Inventory: {config_manager()['player']['inventory']}", message_type="Info", group="Showcase")
Debug.log("Adding Dragon Scale to inventory", message_type="Info", group="Showcase")

current_inventory = config_manager()['player']['inventory']
current_inventory.append("Dragon Scale")
config_manager.update("player.inventory", current_inventory)
Debug.log(f"Updated Inventory: {config_manager()['player']['inventory']}", message_type="Info", group="Showcase")
Debug.log("", message_type="None", group="Showcase")

# Update the progress of the first quest (Defeat the Dragon)
Debug.log(f"Quest Progress (Defeat the Dragon): {config_manager()['quests']['active'][0]['progress']}", message_type="Info", group="Showcase")
config_manager.update("quests.active[0].progress", 80)
Debug.log(f"Updated Quest Progress (Defeat the Dragon): {config_manager()['quests']['active'][0]['progress']}", message_type="Info", group="Showcase")
Debug.log("", message_type="None", group="Showcase")

# Save the updated configuration back to the Newfile
output_dir = 'exsampleFiles/ConfigManager/temp/ConfigManager2.json'
config_manager.save(output_dir)
Debug.log(f"new file saved to {output_dir}:", message_type="Info", group="Showcase")
Debug.log(config_manager(), message_type="Info", group="Showcase")
Debug.log("", message_type="None", group="Showcase")

# Reset the configuration to the default configuration
config_manager.reset()  # No arguments needed because it uses the default config saved when the object is initialized
Debug.log("Configuration Reset:", message_type="Info", group="Showcase")
Debug.log(config_manager(), message_type="Info", group="Showcase")

# Save the updated configuration back to the file
output_dir = 'exsampleFiles/ConfigManager/ConfigManager.json'
config_manager.save(output_dir)
Debug.log("", message_type="None", group="Showcase")

Debug.log(f"Configuration has been saved back to '{output_dir}'", message_type="Info", group="Showcase")

