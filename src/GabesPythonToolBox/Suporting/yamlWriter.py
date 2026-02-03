import os

import yaml


def write_yaml(file_path, data, mode: str = "w"):
    """
    Write a dictionary to a YAML file.
    If mode='a', merge with existing YAML content if it is a dict.
    """
    if mode == "a" and os.path.exists(file_path):
        # Load existing data
        with open(file_path, "r", encoding="utf-8") as f:
            existing_data = yaml.safe_load(f) or {}
        if not isinstance(existing_data, dict):
            raise TypeError("Existing YAML content is not a dict; cannot merge")

        # Merge existing data with new data
        existing_data.update(data)
        data_to_write = existing_data
        mode = "w"  # Overwrite file with merged content
    else:
        data_to_write = data

    with open(file_path, mode=mode, encoding="utf-8") as f:
        yaml.safe_dump(data_to_write, f, sort_keys=False, allow_unicode=True)
