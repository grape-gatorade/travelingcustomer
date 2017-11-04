""" Contains the OptimalPath class, implementing the PathStrategy """
from python.PathStrategyInterface import PathStrategy
from python.Location import Location


class ClosingTimePath(PathStrategy):
    """
        ClosingTime Path implements the PathStrategy Interface.
        calculate_path will be the path organized by closing times in ascending order.
    """


    def calculate_path(self, path_list):
        """
            Returns the ordered closing time path in ascending order.
        """
        for item in path_list:
        	location = Location(item)
        	print location.generateClosingInfo()