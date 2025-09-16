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
