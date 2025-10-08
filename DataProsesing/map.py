from ..Utility.Debug import *

def Map(input,minInput,maxInput,minOutput,maxOutput):
    """ Maps a value from one range to another. 
    
    :param minInput: the lovest value the input shood have
    :param maxInput: the higest value the input shood have
    :param minOutput: the lovest value the output shood have
    :param maxOutput: the higest value the output shood have
    :return: Returns input shifted from one range to another
    """

    Debug.log(f"Map","Header",group="LIB")
    Debug.log(f"input value: {input}, minInput: {minInput}, maxInput: {maxInput}, minOutput: {minOutput}, maxOutput: {maxOutput}","Info",group="LIB")
    
    if not all(isinstance(arg, (int, float)) for arg in (input,minInput,maxInput,minOutput,maxOutput)):
        raise TypeError("All arguments must be numbers (int or float).")

    output = (input - minInput) / (maxInput - minInput) * (maxOutput - minOutput) + minOutput

    Debug.log(f"output value: {output}","Info",group="LIB")
    Debug.log(f"Map","End",group="LIB")

    return output

def ClampMap(input,minInput,maxInput,minOutput,maxOutput):
    """ Maps a value from one range to another. and clamps it to min max output
    
    :param minInput: the lovest value the input shood have
    :param maxInput: the higest value the input shood have
    :param minOutput: the lovest value the output will have
    :param maxOutput: the higest value the output will have
    :return: Returns input shifted from one range to another clamped
    """
    Debug.log(f"ClampMap","Header",group="LIB")
    Debug.log(f"input value: {input}, minInput: {minInput}, maxInput: {maxInput}, minOutput: {minOutput}, maxOutput: {maxOutput}","Info",group="LIB")
    
    if not all(isinstance(arg, (int, float)) for arg in (input,minInput,maxInput,minOutput,maxOutput)):
        raise TypeError("All arguments must be numbers (int or float).")
    
    output = max(min((input - minInput) / (maxInput - minInput) * (maxOutput - minOutput) + minOutput, maxOutput),minOutput)
    Debug.log(f"output value: {output}","Info",group="LIB")
    Debug.log(f"ClampMap","End",group="LIB")
    return output

def Clamp(val:float,minOutput:float=None,maxOutput:float=None)->float: #shood be able to get just max or just min
    """ Clamps the input between 2 values
    
    :param minOutput: the lovest value of the output will have
    :param maxOutput: the higest value the output will have
    :return: Returns input between max,min
    """
    Debug.log(f"Clamp","Header",group="LIB")

    # Validate inputs that are not None
    for name, arg in [("val", val), ("minOutput", minOutput), ("maxOutput", maxOutput)]:
        if arg is not None and not isinstance(arg, (int, float)):
            raise TypeError(f"{name} must be a number (int or float) or None.")
    
    Debug.log(f"input value: {val}, minOutput: {minOutput}, maxOutput: {maxOutput}","Info",group="LIB")

    output = val
    if isinstance(maxOutput, (int, float)):
        output = min(output,maxOutput)
    if isinstance(minOutput, (int, float)):
        output = max(output,minOutput)

    Debug.log(f"output value: {output}","Info",group="LIB")
    Debug.log(f"Clamp","End",group="LIB")
    return output
