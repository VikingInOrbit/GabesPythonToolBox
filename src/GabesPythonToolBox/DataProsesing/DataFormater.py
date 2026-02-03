from ..Utility.Debug import *


def rebase_data(data, visible_keys, col_widths):
    Debug.log(f"rebase_data", "Header", group="LIB")
    Debug.log(f"kees to rebase to {visible_keys}", "Info", group="LIB")

    # tar in data og keys og gir utigjen samme data men kun etter keys
    lines = []

    # Header row
    header_line = " | ".join(
        f"{key.ljust(col_widths.get(key, len(key)))}" for key in visible_keys
    )
    lines.append(f"|{header_line}|")

    data_new = []

    # Data rows
    for row in data:
        new_row = {key: row[key] for key in visible_keys if key in row}
        data_new.append(new_row)

    Debug.log(f"rebase_data", "End", group="LIB")
    return data_new


def merge_data_by(data, sort_key, value_keys: list = []):
    Debug.log(f"merge_data_by", "Header", group="LIB")
    Debug.log(f"merge data to: {sort_key}, and keep {value_keys}", "Info", group="LIB")

    new_data = {}

    for row in data:
        key = row[sort_key]  # e.g., district name
        if key not in new_data:
            # start a new record with 0 for all value_keys
            new_data[key] = {k: 0 for k in value_keys}
            new_data[key][sort_key] = key

        # add up all values in value_keys
        for value in value_keys:
            try:
                new_data[key][value] += float(row[value])
            except ValueError:
                pass  # skip if value is not numeric

    # convert dict back into list of dicts
    new_data = list(new_data.values())

    Debug.log(f"merge_data_by", "End", group="LIB")
    return new_data


def sort_data_by(data, sort_key, reverse=False):
    Debug.log(f"sort_data_by", "Header", group="LIB")
    Debug.log(f"sort_data_by", "End", group="LIB")
    return sorted(data, key=lambda row: row.get(sort_key, ""), reverse=reverse)


def filter_data_cutoff(
    data, key, cutoff, dir: bool = True
):  # dir is direction, if false it discards above cutoff, if true it discards below cutoff
    Debug.log(f"filter_data_cutoff", "Header", group="LIB")

    if dir:
        Debug.log(f"removes below: {cutoff}", "Info", group="LIB")
        Debug.log(f"filter_data_cutoff", "End", group="LIB")
        return [row for row in data if row.get(key, 0) >= cutoff]
    else:
        Debug.log(f"filter_data_cutoff", "End", group="LIB")
        Debug.log(f"removes above: {cutoff}", "Info", group="LIB")
        return [row for row in data if row.get(key, 0) < cutoff]


def helper_column(data, key, new_key, formula):
    Debug.log(f"helper_column", "Header", group="LIB")

    data_new = []
    for row in data:
        # copy the row to avoid modifying original
        new_row = row.copy()

        # get source value, default to 0
        value = new_row.get(key, 0)
        try:
            value = float(value)
        except (ValueError, TypeError):
            Debug.log(
                f"error in phraising new data, value tyed to convert: {value}",
                "Warning",
                group="LIB",
            )
            value = 0

        # add new column
        value = formula(value)

        new_row[new_key] = value
        data_new.append(new_row)

    Debug.log(f"helper_column", "End", group="LIB")
    return data_new
