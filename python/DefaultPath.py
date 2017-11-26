""" Contains the Default class, implementing the PathStrategy """
from python.PathStrategyInterface import PathStrategy
from python.Matrix import Matrix

class DefaultPath(PathStrategy):
    """
        DefaultPath implements the PathStrategy Interface.
        calculate_path will be the path as given
    """


    def calculate_path(self, path_list, start_time):
        """
            Returns the path as given
        """
        if path_list is None:
            return -1

        result = list(range(len(path_list)))
        result.append(0)
        return result
