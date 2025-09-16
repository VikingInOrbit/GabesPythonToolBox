from ..Utility.Debug import *

def count(data, key):
    return len({row[key] for row in data if key in row})

def get_column_widths(data, padding=2): #including headers
    col_widths = {}

    for col in data[0].keys():
        # find longest string among header name + all cell values in this column
        max_len = max(
            [len(str(row.get(col, ""))) for row in data] + [len(col)]
        )
        col_widths[col] = max_len + padding

    return col_widths

def meet_condition(value, marker_value, compare_type="equals"):
    if compare_type == "equals":
        return str(value) == str(marker_value)
    elif compare_type == "gte":  # greater or equal
        try:
            return float(value) >= float(marker_value)
        except ValueError:
            return False
    elif compare_type == "lte":  # less or equal
        try:
            return float(value) <= float(marker_value)
        except ValueError:
            return False
    return False

def position_handler(position,modifier,value):
    if position == "start":  # prepend
        Line = f"{modifier}{value}"
    elif position == "end":  # append
        Line = f"{value}{modifier}"
    elif position == "both":  # append
        Line = f"{modifier}{value}{modifier}"
    else:
        TypeError
    return Line
