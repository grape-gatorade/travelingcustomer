import unittest
from python.Location import Location
from python.ClosingTimePath import ClosingTimePath
from datetime import datetime


class TestStringMethods(unittest.TestCase):

    def test_empty_list(self):
        """Test for when the user inputs no locations"""
        closing = ClosingTimePath()
        input_list = []
        result = closing.calculate_path(input_list, datetime.now())

        #empty path returns 4 empty lists
        self.assertTrue(len(result[0]) == 0)
        self.assertTrue(len(result[1]) == 0)
        self.assertTrue(len(result[2]) == 0)
        self.assertTrue(len(result[3]) == 0)

    def test_single_always_open(self):
        """Test for when user submits only one 24/7 location"""
        closing = ClosingTimePath()
        #hilton in troy, open 24/7
        input_list = ['ChIJ7d-xRZcP3okRYq4CVW3e56k']
        result = closing.calculate_path(input_list, datetime.now())

        #24/7 places are aded to both regular list and 24/7 list
        self.assertTrue(len(result[0]) == 0)
        self.assertTrue(len(result[1]) == 1)
        self.assertTrue(len(result[2]) == 0)
        self.assertTrue(len(result[3]) == 1)

    def test_single_error(self):
        """Test for single location with no known time"""
        closing = ClosingTimePath()

        #philadelphia, PA
        input_list = ['ChIJ60u11Ni3xokRwVg-jNgU9Yk']
        result = closing.calculate_path(input_list, datetime.now())

        #philly has no closing time, it only gets added to error
        self.assertTrue(len(result[0]) == 1)
        self.assertTrue(len(result[1]) == 0)
        self.assertTrue(len(result[2]) == 0)
        self.assertTrue(len(result[3]) == 0)

    def test_multi_error(self):
        """Test for computing 3 separate error locations"""
        closing = ClosingTimePath()

        #philadelphia, PA, albany,ny, new york, ny
        input_list = ['ChIJ60u11Ni3xokRwVg-jNgU9Yk', 'ChIJS_tPzDQK3okRxCjnoBJjoeE', 'ChIJOwg_06VPwokRYv534QaPC8g']
        result = closing.calculate_path(input_list, datetime.now())

        #same as previous test, only all 3 are culprits, they should notbe added anywhere else
        self.assertTrue(len(result[0]) == 3)
        self.assertTrue(len(result[1]) == 0)
        self.assertTrue(len(result[2]) == 0)
        self.assertTrue(len(result[3]) == 0)


    def test_multi_always(self):
        """Test for computing 3 separate error locations"""
        closing = ClosingTimePath()

        #hilton in troy, samaritan hospital in troy
        input_list = ['ChIJ7d-xRZcP3okRYq4CVW3e56k', 'ChIJjZrhSJkP3okR7aNWoQVvGCg']
        result = closing.calculate_path(input_list, datetime.now())

        #same as previous test, only all 3 are culprits, they should notbe added anywhere else
        self.assertTrue(len(result[0]) == 0)
        self.assertTrue(len(result[1]) == 2)
        self.assertTrue(len(result[2]) == 0)
        self.assertTrue(len(result[3]) == 2)

        #24 hour times are 2500, should be stored in tuple alongside index
        self.assertTrue(result[3][0][1] == 2500)
        self.assertTrue(result[3][1][1] == 2500)

    def test_error_and_always(self):
        """Test one error location and one always active location"""
        closing = ClosingTimePath()

        #philadelphia and samaritan hospital in troy
        input_list = ['ChIJ60u11Ni3xokRwVg-jNgU9Yk', 'ChIJjZrhSJkP3okR7aNWoQVvGCg']
        result = closing.calculate_path(input_list, datetime.now())
        self.assertTrue(len(result[0]) == 1)
        self.assertTrue(len(result[1]) == 1)
        self.assertTrue(len(result[2]) == 0)
        self.assertTrue(len(result[3]) == 1)

        #24 hour place should have 2500 listed for closing time in spite of error
        self.assertTrue(result[3][0][1] == 2500)

    def test_single_location_open(self):
        """test if on elocation is oepn or closed"""
        closing = ClosingTimePath()

        #hennings supermarket in PA
        input_list = ['ChIJkfMeIS2fxokRKgvjrsrWagA']
        result = closing.calculate_path(input_list, datetime.now())


        time = datetime.now()
        curr_time = int(time.strftime("%H%M"))

        #if hennings is closed, add it to closed list
        if (curr_time < 700 or curr_time > 2300):
            self.assertTrue(len(result[0]) == 0)
            self.assertTrue(len(result[1]) == 0)
            self.assertTrue(len(result[2]) == 1)
            self.assertTrue(len(result[3]) == 0)

        #not closed, we ran this within the acceptable closing time
        else:
            self.assertTrue(len(result[0]) == 0)
            self.assertTrue(len(result[1]) == 0)
            self.assertTrue(len(result[2]) == 0)
            self.assertTrue(len(result[3]) == 1)
            self.assertTrue(result[3][0][1] == 2300)

    def test_single_and_always(self):
        """Code designed to test that places are sorted correctly"""
        closing = ClosingTimePath()

        #hennings supermarket in PA, hilton in troy
        input_list = ['ChIJkfMeIS2fxokRKgvjrsrWagA', 'ChIJ7d-xRZcP3okRYq4CVW3e56k']
        result = closing.calculate_path(input_list, datetime.now())


        time = datetime.now()
        curr_time = int(time.strftime("%H%M"))

        #if hennings is closed, add it to closed list
        if (curr_time < 700 or curr_time > 2300):
            self.assertTrue(len(result[0]) == 0)
            self.assertTrue(len(result[1]) == 1)
            self.assertTrue(len(result[2]) == 1)
            self.assertTrue(len(result[3]) == 1)
            self.assertTrue(result[3][0][1] == 2500)


        #not closed, we ran this within the acceptable closing time
        else:
            self.assertTrue(len(result[0]) == 0)
            self.assertTrue(len(result[1]) == 1)
            self.assertTrue(len(result[2]) == 0)
            self.assertTrue(len(result[3]) == 2)

            #both locations should appear as open, 24/7 place is last
            self.assertTrue(result[3][0][1] == 2300)
            self.assertTrue(result[3][1][1] == 2500)

    def test_two_not_special(self):
        """Test for 2 locations that have a deifnite closing time"""

        closing = ClosingTimePath()
        #hennings supermarket in PA, wal-mart in Troy
        input_list = ['ChIJkfMeIS2fxokRKgvjrsrWagA', 'ChIJ55INakMF3okRwIYWbgiifaE']
        result = closing.calculate_path(input_list, datetime.now())


        time = datetime.now()
        curr_time = int(time.strftime("%H%M"))

        #both places are closed here
        if (curr_time < 600 and curr_time >= 0):
            self.assertTrue(len(result[0]) == 0)
            self.assertTrue(len(result[1]) == 0)
            self.assertTrue(len(result[2]) == 2)
            self.assertTrue(len(result[3]) == 0)
        
        #only walmart is open
        elif (curr_time >= 600 and curr_time < 700):
            self.assertTrue(len(result[0]) == 0)
            self.assertTrue(len(result[1]) == 0)
            self.assertTrue(len(result[2]) == 1)
            self.assertTrue(len(result[3]) == 1)
            self.assertTrue(result[3][0][1] == 200)

        #both places are now open
        elif (curr_time >= 700 and curr_time < 2300):
            self.assertTrue(len(result[0]) == 0)
            self.assertTrue(len(result[1]) == 0)
            self.assertTrue(len(result[2]) == 0)
            self.assertTrue(len(result[3]) == 2)
            self.assertTrue(result[3][0][1] == 2300)
            self.assertTrue(result[3][1][1] == 0)

        #henning's closed, walmart open
        else:
            self.assertTrue(len(result[0]) == 0)
            self.assertTrue(len(result[1]) == 0)
            self.assertTrue(len(result[2]) == 1)
            self.assertTrue(len(result[3]) == 1)
            self.assertTrue(result[3][0][1] == 0)











if __name__ == '__main__':
    unittest.main()