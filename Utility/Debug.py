import GabesPythonToolBox.Utility.Collor as GTB


class Debug:
    R = GTB.R
    
    # DbugType
    Type = {
        "Header": GTB.FG_Blue + GTB.BG_Black,
        "Error": GTB.BG_B_Red,
        "Fail": GTB.BG_Black + GTB.FG_B_Red,
        "Success": GTB.BG_Black + GTB.FG_B_Green,
        "Warning": GTB.BG_Black + GTB.FG_Yellow,
        "Info": GTB.BG_Black + GTB.FG_Cyan,
        "InProgress": GTB.BG_Cyan + GTB.FG_Black,
    }

    # Static settings for the Debug class
    debug_enabled = True
    groups = {"LIB": False}  # Always have a default group enabled

    @classmethod
    def set_debug_enabled(cls, enabled: bool = True):
        """Turn debugging on or off. Defaults to true."""
        cls.debug_enabled = enabled  # Set the class variable

    @classmethod
    def add_group(cls, group: str, enabled: bool = True):
        """Add a message group."""
        cls.groups[group] = enabled  # Add the group with its enabled status

    @classmethod
    def remove_group(cls, group: str):
        """Remove a message group."""
        if group in cls.groups:
            del cls.groups[group]  # Remove the group from the dictionary

    @classmethod
    def list_groups(cls):
        """List all message groups and their status."""
        return cls.groups  # Return all groups with their status

    @classmethod
    def enable_group(cls, group: str):
        """Enable a specific message group."""
        cls.groups[group] = True  # Set the group's status to enabled

    @classmethod
    def disable_group(cls, group: str):
        """Disable a specific message group."""
        cls.groups[group] = False  # Set the group's status to disabled

    @classmethod
    def log(cls, message: str, message_type: str = "Info", group: str = None, verbosity: int = 1):
        """Log a message."""
        if not cls.debug_enabled:
            return  # Debugging is turned off

        # If a group is provided, only log messages from enabled groups
        if group and not cls.groups.get(group, True):
            return  # Skip messages from disabled groups

        # Retrieve the type for the message type
        Type = cls.Type.get(message_type, "")
        
        match message_type:
            case "Header":
                print(f"{Type}------ {message} ------{cls.R}")
            case "Error":
                print(f"{Type}_-_-_- {message} -_-_-_{cls.R}")
            case "Fail":
                print(f"{Type}{message}{cls.R}")
            case "Success":
                print(f"{Type}{message}{cls.R}")
            case "Warning":
                print(f"{Type}_-_-_- {message} -_-_-_{cls.R}")
            case "Info":
                print(f"{Type}{message}{cls.R}")
            case "InProgress":
                print(f"{Type}{message}{cls.R}")
            case _:
                # Default case if the message type doesn't match any of the above
                print(f"{message}...{cls.R}")
        
