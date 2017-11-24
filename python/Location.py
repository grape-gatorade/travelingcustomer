"""
    This Module contains the location class,
    used to keep track of all location information.
"""
from __future__ import print_function
from datetime import datetime, timedelta
import googlemaps

class Location(object):
    """
        Constructor
        Location contains the id, closing time,
        whether or not the location is open 24 hours a day,
        the original index of this item form the input list,
        a value determining whther the location is open now
        and the time difference between the location's closing time
        versus the current time
    """
    def __init__(self, new_id, index):
        self.__id = new_id
        self.__closing_time = 0
        self.__24hours = False
        self.__index = index
        self.__open_now = "Cannot Tell"
        self.__time_diff = -1



    def __cmp__(self, other):
        """
            Comparator for closing times
            We base sorting on how far off closing time is from current time
        """
        return cmp(self.get_time_diff(), other)


    def set_closing_time(self):
        """
            Makes Google Maps call to determine the closing time for this location.
        """

        #query google mpas with the unique ID to get the location information JSON
        gmaps = googlemaps.Client(key='AIzaSyDA3tCPe5-nZ7i8swYDskytH2cmQq6lBiA')
        location_info = gmaps.place(self.__id, 'English')

        #current time and current day of the week, closing time can change day by day
        now = datetime.now()
        weekday = now.strftime("%w")

        #default opening hours object to be replaced by google maps info
        opening_hours = {}

        #try to get a value for any time based information about the location
        try:
            opening_hours = location_info['result']['opening_hours']

            #place has time information, need to check if it has a closing time
            try:
                self.__closing_time = int(opening_hours['periods'][int(weekday)]['close']['time'])

            #time not available for this day of the week, could either be
            #24 hour case or no closing time
            except IndexError:

                open_info = opening_hours['periods'][0]['open']

                #unique return value for 24 hours case
                if open_info['day'] == 0 and open_info['time'] == '0000':
                    self.__24hours = True
                    self.__closing_time = 2500

                #not 24 hour case, no time available
                else:
                    self.__closing_time = -1

            #can't find closing time info in general for today
            #could be the case of some 24 hour objects
            except KeyError:

                #24/7 case, place is open all the time and has no closing value
                open_info = opening_hours['periods'][0]['open']
                if open_info['day'] == 0 and open_info['time'] == '0000':
                    self.__24hours = True
                    self.__closing_time = 2500
                #not the 24/7 case, place has no time listed for clsing
                else:
                    self.__closing_time = -1

        #place has no time information whatsoever, like a city or a state
        except KeyError:
            self.__closing_time = -1

        #try to see if the place is open now after we figure out closing time
        try:
            is_open = location_info['result']['opening_hours']['open_now']
            self.__open_now = is_open

        #place does not have open now info, leave it as default string
        except KeyError:
            pass


    def set_time_diff(self):
        """
            Computes time difference in seconds between current time and closing time.
            This value determines the order in which the route will be returned.
        """
        #current time
        time = datetime.now()

        #if place isn't open 24 hours and definitively has a closing time
        if (self.__closing_time != 2500) and (self.__closing_time != -1):

            #current time hour and minute in 2400 representation to match google
            curr_hour = int(time.strftime("%H"))
            curr_minute = int(time.strftime("%M"))
            curr_time = int(time.strftime("%H%M"))

            #current time in 24 hour representation in timedelta object for comparison
            curr_time_delta = timedelta(hours=curr_hour, minutes=curr_minute)

            #place Google's 2400 time format into appropriate tme delta object
            close_hour = self.__closing_time/100
            close_minute = self.__closing_time%100
            close_time_delta = timedelta(hours=close_hour, minutes=close_minute)

            #if current time is greater, that means the place is either
            #already closed or the closing time is the next day
            #calculate difference between current itme and midnight,
            #then add the closing time for the next day to calculation
            if curr_time > self.__closing_time:
                baseline = timedelta(hours=24)
                diff = int(((baseline - curr_time_delta) + close_time_delta).total_seconds())
                self.__time_diff = diff

            #the place has not reached its closing time yet for the current day
            #time difference is difference between closing time and now for the current day
            else:
                diff = int(((close_time_delta - curr_time_delta).total_seconds()))
                self.__time_diff = diff

        #if place is open 24 hours, set difference to 86401
        #(24 hours in seconds plus 1, cannot be matched via our subtraction algrotihm)
        elif self.__closing_time == 2500:
            self.__time_diff = 86401


    def get_closing_time(self):
        """ Return closing time """
        return self.__closing_time

    def get_time_diff(self):
        """Returns time difference in seconds between time of query and closing time"""
        return self.__time_diff

    def is_24_hours(self):
        """ Return boolean indicating if place is open is 24/7  """
        return self.__24hours

    def get_index(self):
        """ Return index for path disambiguation """
        return self.__index

    def is_open(self):
        """Returns if location is closed or not"""

        #if stuck at default value, pretend that it is open,
        #we only care about realizing definitive closed locations
        if self.__open_now == "Cannot Tell":
            return True

        return self.__open_now
