"""
    Contains the Matrix object representing 2D distance matrix.
    Matrix also contains methods for solving a greedy TSP approximation.
"""
from __future__ import print_function
from sys import maxsize
from itertools import chain, combinations
from datetime import datetime, timedelta
import time
import googlemaps

""" Begin Helper Classes / Functions for Solving TSP """
class Index(object):
    """
        Index class is used in TSP Solution for keeping track of
        vertex visited and vertex used to visit
    """

    def __init__(self, current_vertex_, vertex_set_):
        """ Constructor """
        self.current_vertex = current_vertex_
        self.vertex_set = frozenset(vertex_set_)

    def __hash__(self):
        return hash((self.current_vertex, self.vertex_set))

    def __eq__(self, other):
        return (other and
                self.current_vertex == other.current_vertex and
                self.vertex_set == other.vertex_set)

    def __ne__(self, other):
        return not self.__eq__(other)

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    given_set = list(iterable)
    return chain.from_iterable(combinations(given_set, r) for r in range(len(given_set)+1))

def subsets(given_list):
    """ Given A List, create a list of all subsets containing elements in that list """
    return list(map(set, powerset(given_list)))


""" End helper classes / functions for solving TSP """
""" Begin Matrix, an implementation of a Graph using an Adjacency Matrix """

class Matrix(object):
    """
        Matrix is designed to handle the distance matrix from Google Maps and stores it as a matrix.
        This matrix is what will be used to determine best path.
    """
    def __init__(self, matrix=None):
        """
            Default constructor
        """
        self._matrix = matrix if matrix != None else []
        self._cannot_find = set([])

    def setup_distance_matrix(self, path_list, travel_type='driving', start_time=None, edge_type='duration'):
        """
            Funciton that sets up the distance matrix.
            Parameters:
            path_list: list of strings containing the names of locations
            travel_type:string indicating travel type
            valid values for travel type are 'driving, 'walking', or 'transit'
        """
        if start_time is None:
            print("enters here")
            start_time = datetime.utcnow() + timedelta(minute=5)

        print(start_time)
        path_len = len(path_list)
        if path_len == 0:
            self._matrix = []
            return
        elif path_len == 1:
            self._matrix = [[0]]
            return

        gmaps = googlemaps.Client(key='AIzaSyBuGbc491h07Hp-ao-6o-dkLmUUX9OG_ho')
        new_matrix = []

        num_rows = len(path_list)

        last_call = datetime.now()
        for i in range(0, num_rows):
            print(path_list[i])
            print(datetime.now())
            print(start_time)
            dist_matrix = gmaps.distance_matrix(path_list[i],   # origin
                                                path_list,      # destination
                                                travel_type,    # travel type
                                                'English',      # language
                                                None,           # things to avoid
                                                'imperial',     # units
                                                start_time,     # departure time
                                                None,           # arrival time
                                                None,           # public transit
                                                None,           # transit preferences
                                                'best_guess')   # Traffic Model
            new_distance_list = []
            location_row = dist_matrix['rows'][0]
            for j in range(0, num_rows):
                try:
                    duration_to_location = location_row['elements'][j][edge_type]['value']

                    #new row adds weight
                    new_distance_list.append(duration_to_location if i != j else 0)

                except KeyError:
                    new_distance_list.append(-1)

            new_matrix.append(new_distance_list) #add new nodes to master list

            # There is a limit on the number of elements requested per second to google maps.
            # We sleep for a second if we will be making large requests to the API.
            if len(path_list) >= 10:
                print((float(len(path_list)) / float(100.0)) + float(0.05) - (datetime.now() - last_call).total_seconds())
                if ((datetime.now() - last_call).total_seconds() < ((float(len(path_list)) / float(100.0)) + float(0.01))):
                    time.sleep((float(len(path_list)) / float(100.0)) + float(0.05) - (datetime.now() - last_call).total_seconds())
                last_call = datetime.now()

        for i in range(0, len(new_matrix)):
            if new_matrix[i].count(-1) > 0:
                self._matrix = []
                return

        self._matrix = new_matrix


    def matrix_solve(self):
        """
            An implementation of the Held-Karp Dynamic Programming Solution for TSP
            This implementation utilizes a helper Index class to connect a vertex I reachable
            From vertex 0 to the set of vertices passed over to reach vertex I.
        """

        # Begin with bounds checking

        if not self._matrix:
            return ([], 0)

        if len(self._matrix) == 1:
            return ([0, 0], 0)

        min_cost_map = {}
        parent_map = {}

        # all sets will contain a list of sets made up of all indices exluding 0,
        # all_sets[0] is the empty set
        all_sets = subsets(range(1, len(self._matrix)))

        # final_set contains only the set that contains all elements except 0
        final_set = all_sets.pop()

        # Begin making indices by looping over sets.
        for vertex_set in all_sets:
            # Loop over the vertices. We will make an index so long as the vertex is not in the set.
            for current_vertex in range(1, len(self._matrix)):
                if current_vertex in vertex_set:
                    continue
                # print("Current Vertex:")
                # print(current_vertex)

                index = Index(current_vertex, vertex_set)

                min_cost = maxsize
                min_prev_vertex = 0


                # Try to determine which vertex in the set to have left from to have the lowest cost
                # Copy the set to avoid shenanigans while iterating over set.
                copied_set = set(vertex_set)
                for prev_vertex in vertex_set:

                    # cost is the cost of coming from the chosen previous vertex,
                    # to the current vertex traversing over all the other vertices in vertex set
                    cost = (self._matrix[prev_vertex][current_vertex] +
                            self.get_cost(copied_set, prev_vertex, min_cost_map))
                    if cost < min_cost:
                        min_cost = cost
                        min_prev_vertex = prev_vertex

                # Handling the empty set, the Cost will be distance from 0 to the current vertex
                # Since our current set is empty we do not travel through any other vertices
                # (empty sequences are false)
                if not vertex_set:
                    min_cost = self._matrix[0][current_vertex]

                min_cost_map[index] = min_cost
                parent_map[index] = min_prev_vertex

        # Final Stage of TSP, Now for 0 as the node to reach from 0
        final_min_cost = maxsize
        prev_vertex = -1
        copied_final_set = set(final_set)
        for vertex in final_set:
            cost = self._matrix[vertex][0] + self.get_cost(copied_final_set, vertex, min_cost_map)
            if cost < final_min_cost:
                final_min_cost = cost
                prev_vertex = vertex

        index = Index(0, final_set)
        parent_map[index] = prev_vertex

        return (self.get_tour(parent_map, len(self._matrix)), final_min_cost)


    def get_tour(self, parent_map, total_vertices):
        """
            From the start vertex and parent map, determines the tour through all vertices
            to reach the start vertex again
        """
        vertex_set = set(range(0, total_vertices))

        start = 0
        stack = []
        while True:
            stack.append(start)
            vertex_set.remove(start)
            index = Index(start, vertex_set)
            if index in parent_map.keys():
                start = parent_map[index]
                if start == 0:
                    stack.append(start)
                    break
        return list(reversed(stack))

    def get_cost(self, vertex_set, vertex, cost_map):
        """
            Determine cost to reach vertex from starting vertex,
            traveling through vertices in vertex_set
        """
        vertex_set.remove(vertex)
        index = Index(vertex, vertex_set)
        cost = cost_map[index]
        vertex_set.add(vertex)
        return cost

    def is_valid_matrix(self):
        """
            Check that the matrix initialized is valid. true if valid, false
        """
        return bool(self._matrix)
