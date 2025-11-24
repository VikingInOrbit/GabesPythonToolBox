import json
import os


def write_json(file_path, data, mode: str = "w"):
    """
    Write a dictionary to a JSON file.
    If mode='a', merge with existing JSON content if it is a dict.
    """
    if mode == "a" and os.path.exists(file_path):
        # Load existing data
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                raise ValueError("Existing JSON content is invalid")
        if not isinstance(existing_data, dict):
            raise TypeError("Existing JSON content is not a dict; cannot merge")

        # Merge existing data with new data
        existing_data.update(data)
        data_to_write = existing_data
        mode = "w"  # overwrite with merged content
    else:
        data_to_write = data

    with open(file_path, mode=mode, encoding="utf-8") as f:
        json.dump(data_to_write, f, indent=4, ensure_ascii=False)
