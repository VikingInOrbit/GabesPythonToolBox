import GabesPythonToolBox.Utility.Collor as GTB
class Debug:
    R = GTB.R
    
    # DbugType
    Type = {
        "Header": GTB.FG_B_White + GTB.BG_Black,
        "Error": GTB.BG_B_Red,
        "Fail": GTB.BG_Black + GTB.FG_B_Red,
        "Success": GTB.BG_Black + GTB.FG_B_Green,
        "Warning": GTB.BG_Yellow + GTB.FG_Black,
        "Info": GTB.BG_Black + GTB.FG_B_White,
        "InProgress": GTB.BG_Black + GTB.FG_Yellow,
        "None": None,
        "End": GTB.FG_B_White + GTB.BG_Black,

        "-": GTB.FG_Black + GTB.BG_Red,
    }

    # Static settings for the Debug class
    debug_enabled = True
    groups = {"LIB": False, "LIB_Debug":False, "exsampleFiles": False, "WarningError":True}  # Always have a default group enabled

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
    def start_debug_loger(cls, file_path:str = "debug/In_relative_dir"):
        """start save log objects to a file"""
        #set cls.file_path
        NotImplementedError

    @classmethod
    def save_to_file(cls, ):
        """save log objects to a file"""
        #save to cls.file_path
        NotImplementedError

    @classmethod
    def log(cls, message: str, message_type: str = "-", group: str = None, verbosity: int = 1):
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
                print(f"\n{cls.R}{Type}------ {message} ------{cls.R}")
            case "Error":
                print(f"\n{cls.R}{Type}_-_-_- {message} -_-_-_{cls.R}\n")
            case "Fail":
                print(f"\n{cls.R}{Type}{message}{cls.R}\n")
            case "Success":
                print(f"{cls.R}{Type}{message}{cls.R}")
            case "Warning":
                print(f"\n{cls.R}{Type}_-_-_- {message} -_-_-_{cls.R}")
            case "Info":
                print(f"{cls.R}{Type}{message}{cls.R}")
            case "InProgress":
                print(f"{cls.R}{Type}{message}{cls.R}")
            case "None":
                print(f"{cls.R}{cls.R}{message}{cls.R}")
            case "End":
                print(f"{cls.R}{Type}............{message}{cls.R}")
            case _:
                # Default case if the message type doesn't match any of the above
                message_type="-"
                # Retrieve the type for the message type
                Type = cls.Type.get(message_type, "")

                print(f"\n{cls.R}{Type}{message}...{cls.R}\n")
        
        #cls.save_to_file(message,message_type,group,verbosity)

        
