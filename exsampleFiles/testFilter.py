from GabesPythonToolBox.Utility.Debug import Debug
#Debug.add_group('LIB', True) #Uncoment for the debug mesages

import GabesPythonToolBox.DataProsesing.filter as GTB

 #TODO Debug 
def test():

    startInt = 1
    endInt = 3
    dataPoints = 5


    avarageFilter = GTB.newFilter(dataPoints, "average")
    avarageFiltered = 0

    for x in range(startInt,endInt):
        print(f"testing input: {x}")
        print(f"output avarageFilter: {avarageFilter(x)}")
        avarageFiltered = avarageFilter(x)

    print(f"\n--------------------------\n")

    newWeightedFilter = GTB.newFilter(dataPoints, "newWeighted")
    newWeightedFiltered = 0
    
    for x in range(startInt,endInt):
        print(f"testing input: {x}")
        print(f"output newWeightedFilter: {newWeightedFilter(x)}")
        newWeightedFiltered = newWeightedFilter(x)

    print(f"\n--------------------------\n")

    oldWeightedFilter = GTB.newFilter(dataPoints, "oldWeighted")
    oldWeightedFiltered = 0
    
    for x in range(startInt,endInt):
        print(f"testing input: {x}")
        print(f"output oldWeightedFilter: {oldWeightedFilter(x)}")
        oldWeightedFiltered = oldWeightedFilter(x)

    print(f"\n--------------------------\n")

    print(f"output avarageFilter: {avarageFiltered}")
    print(f"output newWeightedFilter: {newWeightedFiltered}")
    print(f"output oldWeightedFilter: {oldWeightedFiltered}")

    print(f"\n--------------------------\n")

if __name__ == "__main__":
    test()