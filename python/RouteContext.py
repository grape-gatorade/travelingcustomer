""" Contains the RouteContext class, gives client context for different route algorithms """
class RouteContext(object):
    """
        Maintains a reference to the strategy object of interest for calculations.
        Client side object that chooses route to solve at runtime
    """

    def __init__(self, route_strategy):
        """
            Default Constructor
        """
        self._strategy = route_strategy

    def compute_route(self, locations):
        """
            Calls calculate_path for PathStrategy object
        """
        return self._strategy.calculate_path(locations)
