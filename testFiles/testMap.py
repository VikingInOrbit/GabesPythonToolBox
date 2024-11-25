import map

def test():
    inputMin = 0
    inputMax = 10

    diff = 3

    OutputMin = 0
    OutputMax = 1

    print(f"\n--------------------------\n")
    print(f"Map; minInput: {inputMin}, MaxInput: {inputMax} minOutput: {OutputMin}, maxOutput {OutputMax}\n")


    for x in range(inputMin-diff,inputMax+1+diff):
        mapOutput = map.Map(x,inputMin,inputMax,OutputMin,OutputMax)
        print(f"input : {x}, Output {mapOutput}")

    print(f"\n--------------------------\n")
    print(f"ClampMap; minInput: {inputMin}, MaxInput: {inputMax} minOutput: {OutputMin}, maxOutput {OutputMax}\n")

    for x in range(inputMin-diff,inputMax+1+diff):
        clampMapOutput = map.ClampMap(x,inputMin,inputMax,OutputMin,OutputMax)
        print(f"input : {x}, Output {clampMapOutput}")  
    
    print(f"\n--------------------------\n")
    print(f"Clamp; min: {OutputMin}, max {OutputMax}")

    for x in range(inputMin-diff,inputMax+1+diff):
        clampOutput = map.Clamp(x,OutputMin,OutputMax)
        print(f"input : {x}, Output {clampOutput}")  
    
    print(f"\n--------------------------\n")

    

if __name__ == "__main__":
    test()