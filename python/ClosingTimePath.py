""" Contains the OptimalPath class, implementing the PathStrategy """
from __future__ import print_function
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
            Takes list of location IDs as a parameter
        """

        errors = []      #list of places that we have no info for
        always_open = [] # list of 24/7 places
        regular = []     #places that are open, including 24/7 places
        closed = []      #places that are closed now
        new_index = 0    #original list index

        for place in path_list:
            #create new Location object for each place and find their closing times
            loc = Location(place, new_index)
            loc.set_closing_time()

            #-1 means we can't find closing time, add to errors, don't cimpute time difference
            if loc.get_closing_time() == -1:
                errors.append(loc.get_index())

            #the locaton is open 24 hours a day, set maximum time difference for sorting
            elif loc.is_24_hours():
                loc.set_time_diff()
                always_open.append(loc.get_index())
                regular.append(loc)

            #the location is closed, don't compute time difference
            elif loc.is_open() is False:
                closed.append(loc.get_index())

            #place is open and has a closing time, compute time difference
            else:
                loc.set_time_diff()
                regular.append(loc)

            new_index += 1



        #list to store sorted tuples by closing time, tuple contains index and xlosing time integer
        final_regular = []
        sort_time = sorted(regular)
        for reg in sort_time:
            final_regular.append((reg.get_index(), reg.get_closing_time()))

        #return list of all four lists as a result
        answer = []
        answer.append(errors)
        answer.append(always_open)
        answer.append(closed)
        answer.append(final_regular)

        return answer
