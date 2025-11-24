from ..DataProsesing.DataHelperFunctions import *
from ..Utility.Debug import *


# TODO shood i make the tabele be printed in the Debug format?
def print_table(
    data,
    n: int = 0,
    Topper: str = "",
    edje_seperator: str = "|",
    data_seperator: str = "|",
):
    Debug.log(f"print_table", "Header", group="LIB")

    # Determine if data needs formatting
    if not all(isinstance(d, str) for d in data):
        Debug.log("Data needs to be formatted", "Info", group="LIB")
        line = format_data(
            data, edje_seperator=edje_seperator, data_seperator=data_seperator
        )
    else:
        Debug.log("Data does not need to be formatted", "Info", group="LIB")
        line = data  # already a list of strings

    print()
    total_length = len(line[0]) - (
        2 * len(edje_seperator)
    )  # accounting for edje_seperator at start and end
    Debug.log(f"Total line length: {total_length}", "Info", group="LIB")

    border = f"{edje_seperator}{'-' * total_length}{edje_seperator}"
    print(border)

    # Topper row
    if Topper:
        Debug.log(f"printing topper: {Topper}", "Info", group="LIB")
        topper_line = f"{edje_seperator}{Topper: ^{total_length}}{edje_seperator}"
        print(topper_line)

    print(f"{edje_seperator}{' ' * total_length}{edje_seperator}")

    if n <= 0:
        Debug.log(f"Print hele data", "Info", group="LIB")
        for entry in line:
            print(f"{entry}")
    else:
        n += 2  # accounting for header and n=0
        Debug.log(f"print {n+2} lines", "Info", group="LIB")
        for i in range(min(n, len(line))):
            print(line[i])

    print(f"{edje_seperator}{' ' * total_length}{edje_seperator}")
    print(border)

    Debug.log(f"print_table", "End", group="LIB")


def format_data(data, edje_seperator: str = "|", data_seperator: str = "|"):
    Debug.log(f"format_data", "Header", group="LIB")

    Debug.log(f"Get column with", "Info", group="LIB")

    # Calculate column widths
    col_widths = get_column_widths(data)

    lines = []

    # Header row
    header_cells = [
        f"{key.ljust(col_widths.get(key, len(key)))}" for key in data[0].keys()
    ]
    header_line = f" {data_seperator} ".join(header_cells)
    Debug.log(f"make header line: {header_line}", "Info", group="LIB")
    lines.append(f"{edje_seperator}{header_line}{edje_seperator}")

    # Underline
    underline = f"{edje_seperator}{'-' * len(header_line)}{edje_seperator}"
    lines.append(underline)

    Debug.log(f"format data", "Info", group="LIB")
    # Data rows
    for row in data:
        cells = []
        for key in data[0].keys():
            val = row.get(key, "")
            if isinstance(val, float):
                # If float, show 2 decimals unless it's an integer value
                if val.is_integer():
                    cell = f"{int(val)}"
                    Debug.log(f"val: {val} is integer", "Info", group="LIB")
                else:
                    cell = f"{val:.2f}"
                    Debug.log(f"val: {val} is float", "Info", group="LIB")

            elif isinstance(val, int):
                cell = str(val)
                Debug.log(f"val: {val} is int", "Info", group="LIB")

            else:
                cell = str(val)
                Debug.log(f"val: {val} is str", "Info", group="LIB")

            # pad to column width
            cell = cell.ljust(col_widths.get(key, len(cell)))
            cells.append(cell)

        line = f" {data_seperator} ".join(cells)
        Debug.log(f"finished line: {line}", "Info", group="LIB")
        lines.append(f"{edje_seperator}{line}{edje_seperator}")

    Debug.log(f"format_data", "End", group="LIB")
    return lines
