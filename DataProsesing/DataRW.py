import os
from ..Suporting.csvReader import *
from ..Suporting.jsonReader import *
from ..Suporting.yamlReader import *

from ..Suporting.csvWriter import *
from ..Suporting.jsonWriter import *
from ..Suporting.yamlWriter import *

from ..Utility.Debug import Debug


def write_data(file_path,data, **kwargs):

    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
        Debug.log(f"Dir did not exist, created it: {directory}", "Warning", group="WarningError")

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".json":
        write_json(file_path,data, **kwargs)

    elif ext in (".yaml", ".yml"):
        write_yaml(file_path,data, **kwargs)

    elif ext == ".csv":
        write_csv(file_path,data, **kwargs)

    else:
        print(f"Unsupported file extension: {ext}")
        raise ValueError()

def read_data(file_path, **kwargs):
    """
    Read data from JSON, YAML, or CSV into a list of dictionaries.
    Auto-detects format based on file extension.
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".json":
        return read_json(file_path, **kwargs)

    elif ext in (".yaml", ".yml"):
        return read_ymal(file_path, **kwargs)

    elif ext == ".csv":
        return read_csv(file_path, **kwargs)

    else:
        raise ValueError(f"Unsupported file extension: {ext}")
