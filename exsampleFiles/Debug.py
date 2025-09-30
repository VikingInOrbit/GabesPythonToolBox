from GabesPythonToolBox.Utility.Debug import *
from GabesPythonToolBox.Utility.Logger import *

# Enable debugging
Debug.set_debug_enabled(True,verbosity=4)

# Add some custom message groups
Debug.add_group('LIB', True)
Debug.add_group('Database', False)
Debug.add_group('Showcase', True)

Debug.log("\n\n\n", message_type="None", group="Showcase")
Debug.log("------------------------------------------", message_type="Info", group="Showcase")
 
# Log different types of messages with different Types
Debug.log("Custom Header Message", message_type="Header")
Debug.log("This is an error message", message_type="Error")
Debug.log("This is a failed message", message_type="Fail")
Debug.log("This is a success message", message_type="Success")
Debug.log("This is a warning message", message_type="Warning")
Debug.log("This is an info message", message_type="Info")
Debug.log("This is an in-progress message", message_type="InProgress")
Debug.log("This is an None Format message", message_type="None")
Debug.log("This is an End message", message_type="End")
Debug.log("This has a wrong type", message_type="-")

Debug.log("------------------------------------------", message_type="Info", group="Showcase")
Debug.log("\n\n\n", message_type="None", group="Showcase")

# Using a group filter
Debug.log("This should be shown since 'LIB' is enabled", message_type="Info", group="LIB")
Debug.log("This should NOT be shown since 'Database' is disabled", message_type="Info", group="Database")

# Test enabling/disabling groups dynamically
Debug.enable_group('Database')
Debug.log("This should now be shown since 'Database' is enabled", message_type="Info", group="Database")

Debug.disable_group('LIB')
Debug.log("This should NOT be shown since 'LIB' is now disabled", message_type="Info", group="LIB")

#list group
Debug.log("list groups", message_type="Info", group="Showcase")
Debug.log(Debug.list_groups(), message_type="Info", group="Showcase")

#test to add group
Debug.log("add group test", message_type="Info", group="Showcase")
Debug.add_group("test")

Debug.log("list groups", message_type="Info", group="Showcase")
Debug.log(Debug.list_groups(), message_type="Info", group="Showcase")

#test to remove group
Debug.log("remove group test", message_type="Info", group="Showcase")
Debug.remove_group("test")

Debug.log("list groups", message_type="Info", group="Showcase")
Debug.log(Debug.list_groups(), message_type="Info", group="Showcase")

