from ..Utility.Debug import *
import copy
import csv


def write_csv(
    file_path,
    data,
    seperator_symbol: str = ',',
    float_symbol: str = '.',
    encoding: str = 'utf-8'
):
    """
    Write list-of-dictionaries data to a CSV file.

    :param file_path: Output CSV file path.
    :param data: List of dictionaries [{header: value, ...}, ...].
    :param seperator_symbol: Field separator symbol (default: ',').
    :param float_symbol: Decimal symbol for floats (default: '.').
    :param encoding: File encoding (default: utf-8).
    """
    Debug.log("write_csv", "Header", group="LIB")

    if not data or not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
        Debug.log("Invalid data format for CSV writing", "Error", group="WarningError")
        raise ValueError("Data must be a list of dictionaries.")

    # Make a deep copy to avoid modifying original
    data = copy.deepcopy(data)

    # Extract headers from keys of first dict
    headers = list(data[0].keys())

    try:
        with open(file_path, mode="w", newline="", encoding=encoding) as f:
            writer = csv.DictWriter(f, fieldnames=headers, delimiter=seperator_symbol)
            writer.writeheader()

            for row in data:
                # Format floats with custom float_symbol
                formatted_row = {
                    k: (str(v).replace(".", float_symbol) if isinstance(v, float) else v)
                    for k, v in row.items()
                }
                writer.writerow(formatted_row)

        Debug.log(f"CSV saved to {file_path}", "Info", group="LIB")

    except Exception as e:
        Debug.log(f"Error writing CSV: {e}", "Error", group="WarningError")
        raise

    Debug.log("write_csv", "End", group="LIB")
