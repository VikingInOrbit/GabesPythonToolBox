class Filter:
    def __init__(self, num_points, filter_type="average"):
        self.num_points = num_points
        self.filter_type = filter_type
        self.data_points = []

    def __call__(self, input_value):

        self.data_points.append(input_value)
        if len(self.data_points) > self.num_points:
            self.data_points.pop(0)

        if self.filter_type == "average":
            return self.average()
        
        elif self.filter_type == "newWeighted":
            return self.new_weighted()
        
        elif self.filter_type == "oldWeighted":
            return self.old_weighted()
        
        else:
            raise ValueError(f"Unsupported filter type: {self.filter_type}")

    def average(self):
        """Calculates the simple average of the stored data points."""
        return sum(self.data_points) / len(self.data_points)

    def new_weighted(self):
        """Applies more weight to the newest data point."""
        weights = [i + 1 for i in range(len(self.data_points))]
        weighted_sum = sum(w * d for w, d in zip(weights, self.data_points))
        return weighted_sum / sum(weights)

    def old_weighted(self):
        """Applies more weight to the oldest data point."""
        weights = [len(self.data_points) - i for i in range(len(self.data_points))]
        weighted_sum = sum(w * d for w, d in zip(weights, self.data_points))
        return weighted_sum / sum(weights)

def newFilter(num_points, filter_type="average"):
    """
    Factory function to create a new filter.
    
    :param num_points: Number of data points the filter should remember
    :param filter_type: Type of filter to create (e.g., "average", "newWeighted", "oldWeighted")
    :return: A callable filter instance
    """
    return Filter(num_points, filter_type)

def test():

    startInt = 1
    endInt = 3
    dataPoints = 5


    avarageFilter = newFilter(dataPoints, "average")
    avarageFiltered = 0

    for x in range(startInt,endInt):
        print(f"testing input: {x}")
        print(f"output avarageFilter: {avarageFilter(x)}")
        avarageFiltered = avarageFilter(x)

    print(f"\n--------------------------\n")

    newWeightedFilter = newFilter(dataPoints, "newWeighted")
    newWeightedFiltered = 0
    
    for x in range(startInt,endInt):
        print(f"testing input: {x}")
        print(f"output newWeightedFilter: {newWeightedFilter(x)}")
        newWeightedFiltered = newWeightedFilter(x)

    print(f"\n--------------------------\n")

    oldWeightedFilter = newFilter(dataPoints, "oldWeighted")
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