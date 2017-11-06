""" Unit tests for traveling customer python modules """
import datetime
import googlemaps

from python.OptimalPath import OptimalPath

def test_strategy():
    """ Test function for strategy design pattern implementation """
    return
    # path = OptimalPath()

    # assert path.calculate_path() == "Optimal Path"

def test_gmaps():
    """ Test function for Google Maps API """
    gmaps = googlemaps.Client(key='AIzaSyDA3tCPe5-nZ7i8swYDskytH2cmQq6lBiA')
    matrix = gmaps.distance_matrix(["Wal-Mart, Troy, NY", "Rensselaer Polytechnic Institute"],
                                   ["Wal-Mart, Troy, NY", "Rensselaer Polytechnic Institute"],
                                   "driving", "English", None, "imperial",
                                   datetime.datetime.now(), None, "driving",
                                   None, None)

    travel_info = matrix["rows"][0]["elements"][1]
    assert travel_info["status"] == "OK"

def run_tests():
    """ Runs all tests """
    test_gmaps()
    test_strategy()

if __name__ == '__main__':
    run_tests()
