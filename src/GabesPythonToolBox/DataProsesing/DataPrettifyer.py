# Debug.log(f"","Info",group="LIB")
from ..DataProsesing.DataHelperFunctions import *
from ..Utility.Debug import *


def HMI_prettify_cell(data, value_key, modifier, position: str = "end"):
    Debug.log(f"HMI_prettify_cell", "Header", group="LIB")
    new_data = []
    for row in data:
        if value_key in row:
            value = row[value_key]
            if isinstance(value, float):
                value = f"{value:.2f}"
            row[value_key] = position_handler(position, modifier, value)
        new_data.append(row)

    Debug.log(f"HMI_prettify_cell", "End", group="LIB")
    return new_data


def HMI_prettify_line(
    data,
    change_key,
    marker_key,
    marker_value,
    modifier,
    compare_type: str = "equals",
    position: str = "end",
):
    Debug.log(f"HMI_prettify_line", "Header", group="LIB")

    new_data = []
    for row in data:
        if marker_key in row and change_key in row:
            if meet_condition(row[marker_key], marker_value, compare_type):
                value = row[change_key]
                row[change_key] = position_handler(position, modifier, value)
        new_data.append(row)
    Debug.log(f"HMI_prettify_line", "End", group="LIB")
    return new_data


def HMI_prettify_caracter(data, value_key, target, modifier):
    Debug.log(f"HMI_prettify_caracter", "Header", group="LIB")

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
    Debug.log(f"HMI_prettify_caracter", "End", group="LIB")
    return new_data


def HMI_prettify_Header(data, value_key, modifier):
    Debug.log(f"HMI_prettify_Header", "Header", group="LIB")

    new_data = []
    for row in data:
        if value_key in row:
            # Copy row but replace key
            new_row = {modifier if k == value_key else k: v for k, v in row.items()}
            new_data.append(new_row)
        else:
            new_data.append(row)

    Debug.log(f"HMI_prettify_Header", "End", group="LIB")
    return new_data


def HMI_prettify_date(data, value_key, from_format, to_format):
    import re

    Debug.log(f"HMI_prettify_date", "Header", group="LIB")

    # Split formats into lowercase parts and separators ['dd', '-', 'mm', '-', 'yyyy']
    from_parts_raw = re.split(r"(\W+)", from_format)
    from_parts_lower = [
        p.lower() if not re.match(r"\W+", p) else p for p in from_parts_raw
    ]
    to_parts_raw = re.split(r"(\W+)", to_format)

    new_data = []
    for row in data:
        date_str = row.get(value_key, "")
        if not date_str:
            new_data.append(row)
            continue

        # Extract date parts according to from_format
        date_parts = []
        i = 0
        for part in from_parts_raw:
            if re.match(r"\W+", part):
                i += len(part)
            else:
                date_parts.append(date_str[i : i + len(part)])
                i += len(part)

        # lager dataen i et fromat som kan bli brukt videre
        # p = sererer ut verdier fra seporatorer
        # k = nøkkelen som Ex. yyyy, yy ,mm ,dd
        # v = verdien som hører til hvær nøkkel
        # output Ex. {'dd': '19', 'mm': '11', 'yyyy': '2012'}

        part_map = {
            k: v
            for k, v in zip(
                [p for p in from_parts_lower if not re.match(r"\W+", p)], date_parts
            )
        }

        # Build new date string
        new_date = ""
        for part in to_parts_raw:
            if re.match(r"\W+", part):
                new_date += part
            else:
                p_lower = part.lower()
                if p_lower == "yy" and "yyyy" in part_map:
                    new_date += part_map["yyyy"][-2:]
                elif p_lower in part_map:
                    new_date += part_map[p_lower]
                else:
                    new_date += part
        new_row = row.copy()
        new_row[value_key] = new_date
        new_data.append(new_row)

    Debug.log(f"HMI_prettify_date", "End", group="LIB")
    return new_data
