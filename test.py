""" Unit tests for traveling customer python modules """
from python.OptimalPath import OptimalPath

def test_strategy():
    """ Test function for strategy design pattern implementation """
    path = OptimalPath()

    assert(path.calculate_path() == "Optimal Path")
