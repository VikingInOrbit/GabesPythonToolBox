import os

from GabesPythonToolBox.Utility.Debug import Debug
from GabesPythonToolBox.Utility.Logger import Logger

# Example paths for multiple logs
path1 = "exsampleFiles/LoggerTest/temp/log1.csv"
path2 = "exsampleFiles/LoggerTest/temp/"

# Enable logging and set first logger
Debug.set_log_enabled(path1, enabled=True)

# Add a group and control visibility
Debug.add_group("Showcase", False)  # Enable this group, but dont print it

# Logs that will be written to CSV and optionally printed
Debug.log(f"Saving first log to {path1}", message_type="Info", group="Showcase")
Debug.log("This is written only in log1", message_type="Info", group="Showcase")
Debug.log("HI!", message_type="Info", group="Showcase")

# Switch to second log file
Debug.set_log_enabled(path2, enabled=True)

Debug.log(f"Saving first log to {path2}", message_type="Info", group="Showcase")
Debug.log("This is written only in log2", message_type="Info", group="Showcase")
Debug.log(f"HI! this is an exspeted error", message_type="Error", group="ErrorWarnng")

Debug.add_group("Showcase", True)
Debug.log(
    f"Check the file: {path1}, and at path {path2}",
    message_type="None",
    group="Showcase",
)
