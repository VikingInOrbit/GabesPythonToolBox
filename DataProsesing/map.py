def Map(input,minInput,maxInput,minOutput,maxOutput):
    """ Maps a value from one range to another. """
    output = (input - minInput) / (maxInput - minInput) * (maxOutput - minOutput) + minOutput
    return output

def ClampMap(input,minInput,maxInput,minOutput,maxOutput):
    """ Maps a value from one range to another. and clamps it to min max output """
    output = max(min((input - minInput) / (maxInput - minInput) * (maxOutput - minOutput) + minOutput, maxOutput),minOutput)
    return output

def Clamp(input,min,max):
    output = max(min(input,max),min)
    return output