"""
    Contains the Matrix object representing 2D distance matrix.
    Matrix also contains methods for solving a greedy TSP approximation.
"""
from datetime import datetime
import googlemaps

class Matrix(object):
    """
        Matrix is designed to handle the distance matrix from Google Maps and stores it as a matrix.
        This matrix is what will be used to determine best path.
    """
    def __init__(self):
        """
            Default constructor
        """
        self._matrix = []

    def setup_distance_matrix(self, path_list, travel_type='driving'):
        """
            Funciton that sets up the distance atrix.
            Parameters:
            path_list: list of strings containing the names of locations
            travel_type:string indicating travel type
            valid values for travel type are 'driving, 'walking', or 'transit'
        """
        path_len = len(path_list)
        if path_len == 0:
            self._matrix = []
            return

        #get google maps matrix
        gmaps = googlemaps.Client(key='AIzaSyDA3tCPe5-nZ7i8swYDskytH2cmQq6lBiA')
        dist_matrix = gmaps.distance_matrix(path_list, path_list, travel_type, 'English', None,
                                            'imperial', datetime.now(), None, None, None, None)
        #double for loop that finds the edge weight
        new_matrix = []
        num_rows = len(dist_matrix['rows'])
        for i in range(0, num_rows):
            new_distance_list = []
            location_row = dist_matrix['rows'][i]
            for j in range(0, num_rows):
                duration_to_location = location_row['elements'][j]['duration']['value']
                new_distance_list.append(duration_to_location) #new row adds weight
            new_matrix.append(new_distance_list) #add new noes to master list

        self._matrix = new_matrix

    #pylint: disable-msg=too-many-arguments
    #Justification: paths_per_node and count must be recursive parameters
    def path_traverse(self, source, array, paths_per_node, visits, count):
        """
            This method recursively travels to the shortest neighbor of the
            current node we are visiting.
            Parameters:
            source: the index of the current node we are all_path_lengths
            array: the 2d list reresenting the distanc ematrix
            paths_per_node: list of indicies dictating the current path
            visits: list of indicies that we already visited
            count: current total of the sum of weight in paths_per_node

        """
        shortest = max(array[source]) #can be no more than farthese neighbor
        index = -1
        for j in range(0, len(array[source])):
            if j == source or j in visits: #diagonal or we already visited it
                continue
            elif shortest >= array[source][j]: #new shortest found
                shortest = array[source][j]
                index = j #record index of new shortest along with length

        visits.append(source)
        paths_per_node.append(index)
        count += shortest #add weights to total, also add nodes to path
        path_l = len(paths_per_node)
        array_l = len(array)
        if path_l == array_l: # we visited all nodes, we can stop
            return (paths_per_node, count)

        return self.path_traverse(index, array, paths_per_node, visits, count)

    def matrix_solve(self):
        """
            This method is a greedy implementation of the TSP
            Algorithm visits each node in the matrix and computes
            a path following the shortest neighbor each time.
            The path traversal logic is ahndled in path_traverse.
            Return value is path ou of all nodes with lowest sum
            weights.

        """
        best_paths = [] #list of n paths for n destinations
        all_path_lengths = [] #list of corresponding path lengths
        for node in range(0, len(self._matrix)):
            path = []
            visited = []
            path_length = 0
            path.append(node) #find a path starting form each node
            good_path = self.path_traverse(node, self._matrix, path, visited, path_length)
            print good_path
            best_paths.append(good_path)
            all_path_lengths.append(good_path[1])
        maximum_length = max(all_path_lengths)
        best_index = -1
        for leng_index in range(0, len(all_path_lengths)):
            if maximum_length >= all_path_lengths[leng_index]:
                maximum_length = all_path_lengths[leng_index]
                best_index = leng_index
        #return shortest path out of all paths we found from algorithm
        return best_paths[best_index][0]
