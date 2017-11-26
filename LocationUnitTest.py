import unittest
from python.Location import Location
from datetime import datetime

class TestStringMethods(unittest.TestCase):

    def test_single_location_basic(self):
        """Default Test Case to Test Single Location Creation"""

        #moe's southwest in troy ID
        loc=Location('ChIJ49GRIAsP3okRX-P212e7TJU', 117)
        self.assertTrue(loc.get_closing_time() == 0)
        self.assertTrue(loc.get_time_diff() == -1)
        self.assertFalse(loc.is_24_hours())
        self.assertTrue(loc.get_index() == 117)
        self.assertTrue(loc.is_open())

        #assert that we get the right closing time, basic API call
        loc.set_closing_time(datetime.now())
        self.assertTrue(loc.get_closing_time() == 2300)



    def test_error_location_check(self):
        """test 3 cities for consistency, they have no time info"""

        #philadelphia
        loc1=Location('ChIJ60u11Ni3xokRwVg-jNgU9Yk', 1)
        loc1.set_closing_time(datetime.now())

        #albany
        loc2=Location('ChIJS_tPzDQK3okRxCjnoBJjoeE',2)
        loc2.set_closing_time(datetime.now())

        #new york
        loc3=Location('ChIJOwg_06VPwokRYv534QaPC8g',3)
        loc3.set_closing_time(datetime.now())

        self.assertTrue(loc1.get_closing_time() == -1)
        self.assertTrue(loc1.get_index() == 1)

        self.assertTrue(loc2.get_closing_time() == -1)
        self.assertTrue(loc2.get_index() == 2)

        self.assertTrue(loc3.get_closing_time() == -1)
        self.assertTrue(loc3.get_index() == 3)


    def test_24_hour_locations(self):
        """Test to see closing time values for 24 hour locations"""
        #hilton in troy
        loc1=Location('ChIJ7d-xRZcP3okRYq4CVW3e56k', 11)
        loc1.set_closing_time(datetime.now())

        #samaritan hospital in troy
        loc2=Location('ChIJjZrhSJkP3okR7aNWoQVvGCg',22)
        loc2.set_closing_time(datetime.now())

        self.assertTrue(loc1.get_closing_time() == 2500)
        self.assertTrue(loc1.get_index() == 11)

        self.assertTrue(loc2.get_closing_time() == 2500)
        self.assertTrue(loc2.get_index() == 22)

        #proof thhat place is recognized by Google's unique 24 hour id
        self.assertTrue(loc1.is_24_hours())
        self.assertTrue(loc2.is_24_hours())



    def test_closed_check(self):
        """Test to see if a store is open during a certain time of day"""

        #hennings supermarket, assume open until proven otherwise
        location = Location('ChIJkfMeIS2fxokRKgvjrsrWagA', 123)
        self.assertTrue(location.is_open())

        location.set_closing_time(datetime.now())
        self.assertTrue(location.get_closing_time() == 2300)

        current_time = datetime.now()
        curr_hour = int(current_time.strftime("%H"))

        #opening hours of the store
        if curr_hour < 23 and curr_hour > 7:
             self.assertTrue(location.is_open())
        #closiong hours of the store
        else:
            self.assertFalse(location.is_open())


    def test_time_diff_set(self):
        """Test to check for how certain edge cases set time diff value"""
        #hennings supermarket
        location = Location('ChIJkfMeIS2fxokRKgvjrsrWagA', 123)

        #hilton in troy
        location2 = Location('ChIJ7d-xRZcP3okRYq4CVW3e56k', 456)

        #philadelphia, PA
        location3 = Location('ChIJ60u11Ni3xokRwVg-jNgU9Yk', 789)

        location.set_closing_time(datetime.now())
        location2.set_closing_time(datetime.now())
        location3.set_closing_time(datetime.now())

        self.assertTrue(location.get_closing_time() == 2300)
        self.assertTrue(location2.get_closing_time() == 2500)
        self.assertTrue(location3.get_closing_time() == -1)

        location.set_time_diff(datetime.now())
        location2.set_time_diff(datetime.now())
        location3.set_time_diff(datetime.now())

        self.assertTrue(location.get_time_diff() >= 0 and location.get_time_diff() < 86400)
        self.assertTrue(location2.get_time_diff() == 86401)
        self.assertTrue(location3.get_time_diff() == -1)

    def test_comparison_by_time_diff(self):
        """Test to check for how certain edge cases set time diff value"""
        #moe's southwest in troy ID
        loc=Location('ChIJ49GRIAsP3okRX-P212e7TJU', 117)
        loc.set_closing_time(datetime.now())

        #samaritan hospital in troy
        loc2=Location('ChIJjZrhSJkP3okR7aNWoQVvGCg',22)
        loc2.set_closing_time(datetime.now())

        #new york
        loc3=Location('ChIJOwg_06VPwokRYv534QaPC8g',3)
        loc3.set_closing_time(datetime.now())


        self.assertTrue(loc.get_closing_time() == 2300)
        self.assertTrue(loc2.get_closing_time() == 2500)
        self.assertTrue(loc3.get_closing_time() == -1)

        loc.set_time_diff(datetime.now())
        loc2.set_time_diff(datetime.now())
        loc3.set_time_diff(datetime.now())

        #verify less than operator behavior based on time difference, edge cases will be constant, dynamic locations will not be constant
        self.assertTrue(loc < loc2)
        self.assertTrue(loc3 < loc)
        self.assertTrue(loc3 < loc2)
        self.assertFalse(loc < loc)


if __name__ == '__main__':
    unittest.main()