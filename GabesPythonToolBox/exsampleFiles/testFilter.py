from GabesPythonToolBox.Utility.Debug import Debug

Debug.add_group("Showcase", True)

import GabesPythonToolBox.DataProsesing.filter as GTB


def test():
    Debug.log("Filter Function Showcase", "Header", group="Showcase")

    startInt = 1
    endInt = 3
    dataPoints = 5  # how many datapoints are stored

    filter_types = ["average", "newWeighted", "oldWeighted"]
    final_outputs = {}

    for f_type in filter_types:
        Debug.log(f"Testing {f_type} Filter", "Header", group="Showcase")
        filt = GTB.newFilter(dataPoints, f_type)
        last_output = 0

        for x in range(startInt, endInt):
            Debug.log(f"Testing input: {x}", "Info", group="Showcase")
            last_output = filt(x)
            Debug.log(
                f"Output {f_type} filter: {last_output}", "Info", group="Showcase"
            )

        final_outputs[f_type] = last_output
        Debug.log(
            f"Final output {f_type} filter: {last_output}", "Info", group="Showcase"
        )
        Debug.log(f"End of {f_type} Filter Test", "End", group="Showcase")

    # Summary of all filters
    Debug.log("Final Filter Outputs", "Header", group="Showcase")
    for f_type, value in final_outputs.items():
        Debug.log(f"{f_type} Filter: {value}", "Info", group="Showcase")
    Debug.log("End of Final Filter Outputs", "End", group="Showcase")

    Debug.log("Filter Function Showcase", "End", group="Showcase")


if __name__ == "__main__":
    test()
