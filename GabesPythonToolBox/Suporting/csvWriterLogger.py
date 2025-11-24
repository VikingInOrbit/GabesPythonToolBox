import copy
import csv

# TODO make it one file again
# this is a direct coppy of csvWriter and oly exsists sice circular import isues


def write_csv(
    file_path,
    data,
    seperator_symbol: str = ",",
    float_symbol: str = ".",
    encoding: str = "utf-8",
    mode: str = "w",
    data_mode: str = "all",
):
    """
    Write list-of-dictionaries data to a CSV file.
    """

    if (
        not data
        or not isinstance(data, list)
        or not all(isinstance(d, dict) for d in data)
    ):
        # Debug.log("Invalid data format for CSV writing", "Error", group="WarningError")
        raise ValueError("Data must be a list of dictionaries.")

    # Make a deep copy to avoid modifying original
    data = copy.deepcopy(data)

    # Extract headers from keys of first dict
    headers = list(data[0].keys())

    try:
        with open(file_path, mode=mode, newline="", encoding=encoding) as f:
            writer = csv.DictWriter(f, fieldnames=headers, delimiter=seperator_symbol)
            print_header = False
            print_boady = False

            if data_mode == "all":
                print_header = True
                print_boady = True

            if data_mode == "head":
                print_header = True
                print_boady = False

            if data_mode == "body":
                print_header = False
                print_boady = True

            if data_mode == "none":
                print_header = False
                print_boady = False

            if print_header:
                writer.writeheader()

            if print_boady:

                for row in data:
                    # Format floats with custom float_symbol
                    formatted_row = {
                        k: (
                            str(v).replace(".", float_symbol)
                            if isinstance(v, float)
                            else v
                        )
                        for k, v in row.items()
                    }
                    writer.writerow(formatted_row)

    except Exception as e:

        raise
