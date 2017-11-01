import googlemaps 
from datetime import datetime
import json

class Matrix:
    """
        Matrix is designed to handle the distance matrix from Google Maps and stores it as an array matrix.
        This matrix is what will be used to determine best path.
    """
    def __init__(self):
    	self.matrix = []

    def define_matrix(self):
    	gmaps = googlemaps.Client(key='AIzaSyDA3tCPe5-nZ7i8swYDskytH2cmQq6lBiA')

    	dist_matrix=gmaps.distance_matrix(["Wal-Mart, Troy, NY", "Rensselaer Polytechnic Institute","Samaratin Hopsital, Troy, NY"], ["Wal-Mart, Troy, NY", "Rensselaer Polytechnic Institute", "Samaratin Hopsital, Troy, NY"],
                "driving", "English", None, "imperial",
                 datetime.now(), None, "driving",
                 None, None)

    	m=[]
    	num_rows =  len(dist_matrix["rows"])
    	print num_rows
        for i in range(0, num_rows):
        	new_distance_list = []
        	location_row = dist_matrix["rows"][i]
        	for j in range(0, num_rows):
        		duration_to_location = location_row["elements"][j]["duration"]["value"]
        		new_distance_list.append(duration_to_location);
        	m.append(new_distance_list)
        
        self.matrix = m

        
    	
    	
    	return m




    def path_traverse(self, source, array, paths_per_node, visits, count):
        shortest=max(array[source])
        index = -1
        for j in range(0,len(array[source])):
            if (j==source or j in visits):
                continue
            elif shortest >= array[source][j]:
                shortest = array[source][j]
                index=j
    
        visits.append(source)
        paths_per_node.append(index)
        count += shortest
        if len(paths_per_node) == len(array):
            return (paths_per_node, count)
        else:
            return self.path_traverse(index, array, paths_per_node, visits, count)
    
    
        
    def matrix_solve(self):
        best_paths=[]
        all_path_lengths=[]
        for node in range(0, len(self.matrix)):
            path=[]
            visited=[]
            path_length=0
            path.append(node)
            good_path = self.path_traverse(node, self.matrix, path, visited,path_length)
            print good_path
            best_paths.append(good_path)
            all_path_lengths.append(good_path[1])
        
        maximum_length=max(all_path_lengths)
        best_index=-1
        for leng_index in range(0, len(all_path_lengths)):
            if maximum_length >= all_path_lengths[leng_index]:
                maximum_length = all_path_lengths[leng_index]
                best_index=leng_index
    
        return best_paths[best_index][0]
    
