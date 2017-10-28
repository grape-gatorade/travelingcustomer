""" Contains the OptimalPath class, implementing the PathStrategy """
from python.PathStrategyInterface import PathStrategy


class OptimalPath(PathStrategy):
    """
        OptimalPath implements the PathStrategy Interface.
        calculate_path will be the path best fitting our algorithm.
    """

    def calculate_path(self):
        """
            Returns the optimal path:
            as determined by the Traveling Salesman Algorithm.
        """
        return "Optimal Path"
