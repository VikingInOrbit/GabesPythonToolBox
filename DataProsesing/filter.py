from ..Utility.Debug import *

class Filter:
    def __init__(self, num_points, filter_type="average"):
        self.num_points = num_points
        self.filter_type = filter_type
        self.data_points = []

        Debug.log(f"Filter init","Header",group="LIB")
        Debug.log(f"filter_type: {self.filter_type}, num_points: {self.num_points}","Info",group="LIB")
        Debug.log(f"Filter init","End",group="LIB")

    def __call__(self, input_value):

        Debug.log(f"Filter call","Header",group="LIB")
        Debug.log(f"input_value: {input_value}","Info",group="LIB")
        
        self.data_points.append(input_value)
        if len(self.data_points) > self.num_points:
            Debug.log(f"Data Points are full removed oldest","Info",group="LIB")
            self.data_points.pop(0)

        if self.filter_type == "average":
            return self.average()
        
        elif self.filter_type == "newWeighted":
            return self.new_weighted()
        
        elif self.filter_type == "oldWeighted":
            return self.old_weighted()
        
        else:
            Debug.log(f"Filter call","End",group="LIB")
            raise ValueError(f"Unsupported filter type: {self.filter_type}")

    def average(self):
        """Calculates the simple average of the stored data points."""
        Debug.log(f"average Filter","Header",group="LIB")
        
        
        sum = sum(self.data_points) / len(self.data_points)
        Debug.log(f"output sum: {sum}","Info",group="LIB")
        Debug.log(f"average Filter","End",group="LIB")

        return sum

    def new_weighted(self):
        """Applies more weight to the newest data point."""
        Debug.log(f"new weighted Filter","Header",group="LIB")

        weights = [i + 1 for i in range(len(self.data_points))]
        weighted_sum = sum(w * d for w, d in zip(weights, self.data_points))
        sum = weighted_sum / sum(weights)
        Debug.log(f"output sum: {sum}","Info",group="LIB")
        Debug.log(f"new weighted Filter","End",group="LIB")
        
        return sum

    def old_weighted(self):
        """Applies more weight to the oldest data point."""
        Debug.log(f"old weighted Filter","Header",group="LIB")

        weights = [len(self.data_points) - i for i in range(len(self.data_points))]
        weighted_sum = sum(w * d for w, d in zip(weights, self.data_points))
        sum = weighted_sum / sum(weights)
        Debug.log(f"output sum: {sum}","Info",group="LIB")
        Debug.log(f"old weighted Filter","End",group="LIB")
    
        return sum

def newFilter(num_points: int = 20, filter_type: str ="average"):
    """
    Factory to create a new filter.
    
    :param num_points: Number of data points the filter should remember
    :param filter_type: Type of filter to create ("average", "newWeighted", "oldWeighted")
    :return: A callable filter instance
    """
    Debug.log(f"Creating new filter","Header",group="LIB")
    Debug.log(f"with num_points: {num_points} and filter_type: {filter_type}","Info",group="LIB")
    Debug.log(f"Creating new filter","End",group="LIB")
    return Filter(num_points, filter_type)
