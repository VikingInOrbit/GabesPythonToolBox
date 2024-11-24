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

def Clamp(input,min,max):
    """ Clamps the input between 2 values
    
    :param min: the lovest value of the output will have
    :param max: the higest value the output will have
    :return: Returns input between max,min
    """

    if not all(isinstance(arg, (int, float)) for arg in (input, min, max)):
        raise TypeError("All arguments must be numbers (int or float).")

    output = max(min(input,max),min)
    return output