from ..Utility.Debug import *

# from ..Utility.Debug import *
# from GabesPythonToolBox.Utility.Debug import Debug


def process_line(
    line: str, seperator_symbol: str = ",", float_symbol: str = "."
) -> list:
    Debug.log(f"process_line", "Header", group="LIB")

    line = line.strip()
    if not line:
        Debug.log(f"No line", "Info", group="LIB_Debug")
        Debug.log(f"process_line", "End", group="LIB_Debug")
        return []

    if seperator_symbol != ",":
        line = line.replace(float_symbol, ",")
        Debug.log(f"replace seperator_symbol", "Info", group="LIB_Debug")

    if float_symbol != ".":
        line = line.replace(float_symbol, ".")
        Debug.log(f"replace float_symbol", "Info", group="LIB_Debug")

    values = [v.strip() for v in line.split(seperator_symbol)]
    Debug.log(f"Line: {values}", "Info", group="LIB_Debug")

    Debug.log(f"process_line", "End", group="LIB")
    return values


def read_csv(
    file_path,
    seperator_symbol: str = ",",
    float_symbol: str = ".",
    read_from: str = "",
    read_n_lines: int = 0,
    encoding: str = "utf-8",
):
    Debug.log(f"read_csv", "Header", group="LIB")

    data = []
    header = []

    with open(file_path, "r", encoding=encoding) as csv_file:

        # Read header
        header_line = csv_file.readline()
        header = process_line(header_line, seperator_symbol, float_symbol)

        # Decide which lines to read
        if read_from == "head" and read_n_lines > 0:
            Debug.log(f"head", "Header", group="LIB")

            lines = []
            for _ in range(read_n_lines):
                line = csv_file.readline()
                if not line:  # stop if end of file
                    Debug.log(f"No more lines", "Info", group="LIB")
                    break
                lines.append(line)
            Debug.log(f"head", "End", group="LIB")

        elif read_from == "tail" and read_n_lines > 0:
            Debug.log(f"tail", "Header", group="LIB")
            buffer = []
            for line in csv_file:
                if len(buffer) < read_n_lines:
                    buffer.append(line)
                    Debug.log(f"add line to buffer", "Info", group="LIB")
                else:
                    buffer.pop(0)
                    buffer.append(line)
                    Debug.log(f"pop and add line to buffer", "Info", group="LIB")
            lines = buffer

        else:
            Debug.log(f"all", "Header", group="LIB")
            lines = csv_file
            Debug.log(f"all", "End", group="LIB")

        # Process each line using the helper
        for line in lines:
            values = process_line(line, seperator_symbol, float_symbol)
            if not values:
                Debug.log(f"emty row", "Info", group="LIB_Debug")
                continue  # skip empty lines
            row = {header[i]: values[i] for i in range(len(header))}
            Debug.log(f"row:\n{row}\n\n", "Info", group="LIB_Debug")
            data.append(row)

    Debug.log(f"Read data: \n {data}\n", "Info", group="LIB")
    Debug.log(f"read_csv", "End", group="LIB")
    return data
