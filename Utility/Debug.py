from ..Utility.Collor import * 
from ..Utility.Logger import *
import inspect

#TODO how can the buger get where the call (filr line) was from?

class Debug:
    R = R
    
    # DbugType
    Type = {
        "Header": FG_B_White + BG_Black,
        "Error": BG_B_Red,
        "Fail": BG_Black + FG_B_Red,
        "Success": BG_Black + FG_B_Green,
        "Warning": BG_Yellow + FG_Black,
        "Info": BG_Black + FG_B_White,
        "InProgress": BG_Black + FG_Yellow,
        "None": None,
        "End": FG_B_White + BG_Black,

        "-": FG_Black + BG_Red,
    }

    # Static settings for the Debug class
    debug_enabled = True
    logger_enabled = False
    logger = None
    path:str=None
    groups = {"LIB": False, "LIB_Debug":False, "exsampleFiles": False, "WarningError":True}  # Always have a default group enabled
    verbosity = 1

    @classmethod
    def set_debug_enabled(cls, enabled: bool = True,verbosity:int = 1):
        """Turn debugging on or off. Defaults to true."""
        cls.debug_enabled = enabled  # Set the class variable
        cls.verbosity = verbosity

    @classmethod
    def set_log_enabled(cls,path:str=None, enabled: bool = False):
        """Turn logging on or off. Defaults to False."""

        if not enabled:
            return
        
        Logger.start_logger(path)
        
        cls.logger_enabled = enabled  # Set the class variable
        #cls.logger = Logger
        

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
    def log(cls, message: str, message_type: str = "-", group: str = None):
        """Log a message."""

        #sends the message to logbefore desiding to print it in terminal

        frame = inspect.currentframe().f_back
        info = inspect.getframeinfo(frame)

        verbose = ""
        if cls.verbosity >= 2:
            verbose += f" : {info.filename}"
        if cls.verbosity >= 3:
            verbose += f":{info.lineno}"
 
        if cls.logger_enabled:
            Logger.log(message=message,message_type=message_type,group=group,verbose = info)

        if not cls.debug_enabled:
            return  # Debugging is turned off

        # If a group is provided, only log messages from enabled groups
        if group and not cls.groups.get(group, True):
            return  # Skip messages from disabled groups

        

        # Retrieve the type for the message type
        Type = cls.Type.get(message_type, "")

        match message_type:
            case "Header":
                print(f"\n{cls.R}{Type}------ {message} ------{verbose}{cls.R}")
            case "Error":
                print(f"\n{cls.R}{Type}_-_-_- {message} -_-_-_{verbose}{cls.R}\n")
            case "Fail":
                print(f"\n{cls.R}{Type}{message}{verbose}{cls.R}\n")
            case "Success":
                print(f"{cls.R}{Type}{message}{verbose}{cls.R}")
            case "Warning":
                print(f"\n{cls.R}{Type}_-_-_- {message} -_-_-_{verbose}{cls.R}")
            case "Info":
                print(f"{cls.R}{Type}{message}{verbose}{cls.R}")
            case "InProgress":
                print(f"{cls.R}{Type}{message}{verbose}{cls.R}")
            case "None":
                print(f"{cls.R}{cls.R}{message}{verbose}{cls.R}")
            case "End":
                print(f"{cls.R}{Type}............{message}{verbose}{cls.R}")
            case _:
                # Default case if the message type doesn't match any of the above
                message_type="-"
                # Retrieve the type for the message type
                Type = cls.Type.get(message_type, "")
                verbose = ""
                verbose += f" : {info.filename}"
                verbose += f":{info.lineno}"

                print(f"\n{cls.R}{Type}{message}...{verbose}{cls.R}\n")
        
        #cls.save_to_file(message,message_type,group,verbosity)

        
