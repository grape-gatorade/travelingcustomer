""" Contains the DistancePath class, implementing the PathStrategy """
from python.PathStrategyInterface import PathStrategy
from python.Matrix import Matrix

class DistancePath(PathStrategy):
    """
        OptimalPath implements the PathStrategy Interface.
        calculate_path will be the path best fitting our algorithm.
    """


    def calculate_path(self, path_list, start_time):
        """
            Returns a tuple in a format: (list containing Optimal Path, total time spent traveling.)
            as determined by the Greedy Approximation of Traveling Salesman Algorithm.
        """
        if path_list is None:
            path_list = []
        opt_matrix = Matrix()
        opt_matrix.setup_distance_matrix(path_list, 'driving', start_time, 'distance')
        if not opt_matrix.is_valid_matrix():
            return -1

        return_tuple = opt_matrix.matrix_solve()

        return return_tuple