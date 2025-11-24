from ..Utility.Debug import *


def count(data, key):
    Debug.log(f"count", "Header", group="LIB")

    length = len({row[key] for row in data if key in row})

    Debug.log(f"Count: {length}", "Info", group="LIB")
    Debug.log(f"count", "End", group="LIB")
    return length


def get_column_widths(data, padding=2):  # including headers
    Debug.log(f"get_column_widths", "Header", group="LIB")

    col_widths = {}

    for col in data[0].keys():
        # find longest string among header name + all cell values in this column
        max_len = max([len(str(row.get(col, ""))) for row in data] + [len(col)])
        col_widths[col] = max_len + padding
        Debug.log(f"{col} clolom length: {col_widths[col]}", "Info", group="LIB")

    Debug.log(f"get_column_widths", "End", group="LIB")
    return col_widths


def meet_condition(value, marker_value, compare_type="equals"):
    Debug.log(f"meet_condition", "Header", group="LIB")
    if compare_type == "equals":
        Debug.log(f"chek if equal", "Info", group="LIB")
        Debug.log(f"meet_condition", "End", group="LIB")
        return str(value) == str(marker_value)

    elif compare_type == "gte":  # greater or equal
        try:
            Debug.log(f"chek if greater or equal", "Info", group="LIB")
            Debug.log(f"meet_condition", "End", group="LIB")
            return float(value) >= float(marker_value)
        except ValueError:
            Debug.log(f"error greater or equal", "Info", group="LIB")
            Debug.log(f"meet_condition", "End", group="LIB")
            return False

    elif compare_type == "lte":  # less or equal
        try:
            Debug.log(f"chek if less or equal", "Error", group="LIB")
            Debug.log(f"meet_condition", "End", group="LIB")
            return float(value) <= float(marker_value)

        except ValueError:
            Debug.log(f"error less or equal", "Error", group="LIB")
            Debug.log(f"meet_condition", "End", group="LIB")
            return False

    Debug.log(f"compare_type not found", "Error", group="LIB")
    Debug.log(f"meet_condition", "End", group="LIB")
    return False


def position_handler(position, modifier, value):
    Debug.log(f"position_handler", "Header", group="LIB")

    if position == "start":  # prepend
        Debug.log(
            f"add modefier {modifier} to {value} before value", "Info", group="LIB"
        )
        Line = f"{modifier}{value}"
    elif position == "end":  # append
        Debug.log(
            f"add modefier {modifier} to {value} after value", "Info", group="LIB"
        )
        Line = f"{value}{modifier}"
    elif position == "both":  # append
        Debug.log(
            f"add modefier {modifier} to {value} before and after value",
            "Info",
            group="LIB",
        )
        Line = f"{modifier}{value}{modifier}"
    else:
        Debug.log(f"position error: {position}", "Error", group="LIB")
        TypeError

    Debug.log(f"position_handler", "End", group="LIB")
    return Line
