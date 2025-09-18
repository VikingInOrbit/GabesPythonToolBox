from ..Utility.Debug import *
from ..DataProsesing.DataHelperFunctions import *

def HMI_prettify_cell(data, value_key, modifier, position: str = "end"):
    new_data = []
    for row in data:
        if value_key in row:
            value = row[value_key]
            if isinstance(value, float):
                value = f"{value:.2f}"
            row[value_key] = position_handler(position,modifier,value)
        new_data.append(row)
    return new_data

def HMI_prettify_line(data, change_key, marker_key, marker_value, modifier, compare_type: str = "equals", position: str = "end"):

    new_data = []
    for row in data:
        if marker_key in row and change_key in row:
            if meet_condition(row[marker_key], marker_value, compare_type):
                value = row[change_key]
                row[change_key] = position_handler(position,modifier,value)
        new_data.append(row)
    return new_data

def HMI_prettify_caracter(data, value_key, target, modifier):

    new_data = []
    for row in data:
        if value_key in row:
            value = row[value_key]
            # Convert to string in case it's numeric
            value_str = str(value)
            # Replace target with modifier
            value_str = value_str.replace(target, modifier)
            row[value_key] = value_str
        new_data.append(row)
    return new_data

def HMI_prettify_Header(data, value_key, modifier):
    new_data = []
    for row in data:
        if value_key in row:
            # Copy row but replace key
            new_row = {modifier if k == value_key else k: v for k, v in row.items()}
            new_data.append(new_row)
        else:
            new_data.append(row)
    return new_data
