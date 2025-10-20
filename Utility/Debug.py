from ..Utility.Collor import * 
from ..Utility.Logger import *
import inspect
from enum import Enum
from typing import Union

#TODO how can the buger get where the call (filr line) was from?
class LogType(Enum):
    Header = "Header"
    Error = "Error"
    Fail = "Fail"
    Success = "Success"
    Warning = "Warning"
    Info = "Info"
    InProgress = "InProgress"
    NoneType = "None" 
    End = "End"

    Dash = "-"

from enum import Enum
class LogGroup(Enum):
    LIB = "LIB"
    LIB_Debug = "LIB_Debug"
    ExampleFiles = "exsampleFiles"
    WarningError = "WarningError"
    Showcase = "Showcase"


class Debug:
    R = R
        
    # DbugType
    Type = {
        LogType.Header.value: FG_B_White + BG_Black,
        LogType.Error.value: BG_B_Red,
        LogType.Fail.value: BG_Black + FG_B_Red,
        LogType.Success.value: BG_Black + FG_B_Green,
        LogType.Warning.value: BG_Yellow + FG_Black,
        LogType.Info.value: BG_Black + FG_B_White,
        LogType.InProgress.value: BG_Black + FG_Yellow,
        LogType.NoneType.value: None,
        LogType.End.value: FG_B_White + BG_Black,
        LogType.Dash.value: FG_Black + BG_Red,
    }

    groups = {
        LogGroup.LIB.value: False,
        LogGroup.LIB_Debug.value: False,
        LogGroup.ExampleFiles.value: False,
        LogGroup.WarningError.value: True,
        LogGroup.Showcase.value: True
    }

    # Static settings for the Debug class
    debug_enabled = True
    logger_enabled = False
    logger = None
    path:str=None
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
    def log(cls, message: str, message_type: Union[str, LogType] = LogType.Dash, group: Union[str, LogGroup, None] = None):
        """Log a message."""

        # Convert message_type to string if Enum
        if isinstance(message_type, LogType):
            message_type = message_type.value
        
        # Convert group to string if Enum
        if isinstance(group, LogGroup):
            group = group.value

        #sends the message to logbefore desiding to print it in terminal

        frame = inspect.currentframe().f_back
        info = inspect.getframeinfo(frame)

        verbose = ""
        if cls.verbosity >= 2:
            verbose += f" : {info.filename}"
        if cls.verbosity >= 3:
            verbose += f":{info.function}"    
        if cls.verbosity >= 4:
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
                print(f"{cls.R}{Type}_-_-_- {message} -_-_-_{verbose}{cls.R}")
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

        
