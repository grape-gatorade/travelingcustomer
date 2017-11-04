""" Contains the OptimalPath class, implementing the PathStrategy """
from python.PathStrategyInterface import PathStrategy
from python.Matrix import Matrix

class OptimalPath(PathStrategy):
    """
        OptimalPath implements the PathStrategy Interface.
        calculate_path will be the path best fitting our algorithm.
    """


    def calculate_path(self, path_list=[]):
        """
            Returns the optimal path:
            as determined by the Greedy Approximation of Traveling Salesman Algorithm.
        """
        opt_matrix = Matrix()
        opt_matrix.setup_distance_matrix(path_list)
        best_route_indicies = opt_matrix.matrix_solve()
        return_route = []
        for index in best_route_indicies:
            return_route.append(path_list[index])

        return return_route
