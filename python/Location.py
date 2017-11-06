"""
    This Module contains the location class,
    used to keep track of all location information.
"""
from __future__ import print_function
from datetime import datetime
import googlemaps

class Location(object):
    """
        Location contains the id, closing time,
        and whether or not the location is open 24 hours
    """
    def __init__(self, new_id):
        self.__id = new_id
        self.__closing_time = 0
        self.__24hours = False


    def __lt__(self, other):
        return self.__closing_time < other.get_closing_time


    def set_closing_time(self):
        """
            Make Google Maps call to determine the closing time for this location.
        """
        gmaps = googlemaps.Client(key='AIzaSyDA3tCPe5-nZ7i8swYDskytH2cmQq6lBiA')
        location_info = gmaps.place(self.__id, 'English')
        now = datetime.now()
        weekday = now.strftime("%w")

        opening_hours = location_info['result']['opening_hours']
        try:
            print(opening_hours['periods'][int(weekday)]['close']['time'])

        except IndexError:
            open_info = opening_hours['periods'][0]['open']
            if open_info['day'] == 0 and open_info['time'] == '0000':
                self.__24hours = True
            else:
                self.__closing_time = -1

        except KeyError:
            open_info = opening_hours['periods'][0]['open']
            if open_info['day'] == 0 and open_info['time'] == '0000':
                self.__24hours = True
            else:
                self.__closing_time = -1

        print(self.__24hours)

    def get_closing_time(self):
        """ Return closing time """
        return self.__closing_time
