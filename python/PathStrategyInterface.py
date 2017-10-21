""" Module provides Abstract Path Strategy Class to be implemented """
from abc import ABCMeta, abstractmethod

class PathStrategy(object):
    """ Abstract Base Class for Path classes to implement """
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate_path(self):
        """ Function will return locations in recommended order of visiting """
        pass
    