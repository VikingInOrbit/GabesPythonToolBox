from GabesPythonToolBox.Utility.Debug import Debug
Debug.add_group('Showcase', True)

import GabesPythonToolBox.DataProsesing.map as GTB

def test():
    Debug.log("Map and Clamp Showcase", "Header", group="Showcase")

    inputMin = 0
    inputMax = 10
    diff = 3
    OutputMin = 0
    OutputMax = 1

    # Map function
    Debug.log("Testing Map function", "Header", group="Showcase")
    Debug.log(f"Map; minInput: {inputMin}, MaxInput: {inputMax}, minOutput: {OutputMin}, maxOutput: {OutputMax}", "Info", group="Showcase")
    for x in range(inputMin - diff, inputMax + 1 + diff):
        mapOutput = GTB.Map(x, inputMin, inputMax, OutputMin, OutputMax)
        Debug.log(f"Input: {x}, Output: {mapOutput}", "Info", group="Showcase")
    Debug.log("End of Map function test", "End", group="Showcase")

    # ClampMap function
    Debug.log("Testing ClampMap function", "Header", group="Showcase")
    Debug.log(f"ClampMap; minInput: {inputMin}, MaxInput: {inputMax}, minOutput: {OutputMin}, maxOutput: {OutputMax}", "Info", group="Showcase")
    for x in range(inputMin - diff, inputMax + 1 + diff):
        clampMapOutput = GTB.ClampMap(x, inputMin, inputMax, OutputMin, OutputMax)
        Debug.log(f"Input: {x}, Output: {clampMapOutput}", "Info", group="Showcase")
    Debug.log("End of ClampMap function test", "End", group="Showcase")

    # Clamp function
    Debug.log("Testing Clamp function", "Header", group="Showcase")
    Debug.log(f"Clamp; min: {OutputMin}, max: {OutputMax}", "Info", group="Showcase")
    for x in range(inputMin - diff, inputMax + 1 + diff):
        clampOutput = GTB.Clamp(x, OutputMin, OutputMax)
        Debug.log(f"Input: {x}, Output: {clampOutput}", "Info", group="Showcase")
    Debug.log("End of Clamp function test", "End", group="Showcase")

    Debug.log("Map and Clamp Showcase Complete", "End", group="Showcase")


if __name__ == "__main__":
    test()
