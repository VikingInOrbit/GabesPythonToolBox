def Map(input,minInput,maxInput,minOutput,maxOutput):
    """ Maps a value from one range to another. 
    
    :param minInput: the lovest value the input shood have
    :param maxInput: the higest value the input shood have
    :param minOutput: the lovest value the output shood have
    :param maxOutput: the higest value the output shood have
    :return: Returns input shifted from one range to another
    """
    if not all(isinstance(arg, (int, float)) for arg in (input,minInput,maxInput,minOutput,maxOutput)):
        raise TypeError("All arguments must be numbers (int or float).")

    output = (input - minInput) / (maxInput - minInput) * (maxOutput - minOutput) + minOutput
    return output

def ClampMap(input,minInput,maxInput,minOutput,maxOutput):
    """ Maps a value from one range to another. and clamps it to min max output
    
    :param minInput: the lovest value the input shood have
    :param maxInput: the higest value the input shood have
    :param minOutput: the lovest value the output will have
    :param maxOutput: the higest value the output will have
    :return: Returns input shifted from one range to another clamped
    """

    if not all(isinstance(arg, (int, float)) for arg in (input,minInput,maxInput,minOutput,maxOutput)):
        raise TypeError("All arguments must be numbers (int or float).")

    output = max(min((input - minInput) / (maxInput - minInput) * (maxOutput - minOutput) + minOutput, maxOutput),minOutput)
    return output

def Clamp(input,minOutput,maxOutput):
    """ Clamps the input between 2 values
    
    :param minOutput: the lovest value of the output will have
    :param max: the higest value the output will have
    :return: Returns input between max,min
    """

    if not all(isinstance(arg, (int, float)) for arg in (input, minOutput, maxOutput)):
        raise TypeError("All arguments must be numbers (int or float).")

    output = max(min(input,maxOutput),minOutput)
    return output

def test():
    inputMin = 0
    inputMax = 10

    diff = 3

    OutputMin = 0
    OutputMax = 1

    print(f"\n--------------------------\n")
    print(f"Map; minInput: {inputMin}, MaxInput: {inputMax} minOutput: {OutputMin}, maxOutput {OutputMax}\n")


    for x in range(inputMin-diff,inputMax+1+diff):
        mapOutput = Map(x,inputMin,inputMax,OutputMin,OutputMax)
        print(f"input : {x}, Output {mapOutput}")

    print(f"\n--------------------------\n")
    print(f"ClampMap; minInput: {inputMin}, MaxInput: {inputMax} minOutput: {OutputMin}, maxOutput {OutputMax}\n")

    for x in range(inputMin-diff,inputMax+1+diff):
        clampMapOutput = ClampMap(x,inputMin,inputMax,OutputMin,OutputMax)
        print(f"input : {x}, Output {clampMapOutput}")  
    
    print(f"\n--------------------------\n")
    print(f"Clamp; min: {OutputMin}, max {OutputMax}")

    for x in range(inputMin-diff,inputMax+1+diff):
        clampOutput = Clamp(x,OutputMin,OutputMax)
        print(f"input : {x}, Output {clampOutput}")  
    
    print(f"\n--------------------------\n")

    

if __name__ == "__main__":
    test()