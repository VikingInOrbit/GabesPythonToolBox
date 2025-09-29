import os
from ..Suporting.csvReader import *
from ..Suporting.jsonReader import *
from ..Suporting.yamlReader import *

from ..Suporting.csvWriter import *
from ..Suporting.jsonWriter import *
from ..Suporting.yamlWriter import *

def write_data(file_path, **kwargs):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".json":
        return write_json(file_path)

    elif ext in (".yaml", ".yml"):
        return write_yaml(file_path)

    elif ext == ".csv":
        return write_csv(file_path, **kwargs)

    else:
        raise ValueError(f"Unsupported file extension: {ext}")

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
