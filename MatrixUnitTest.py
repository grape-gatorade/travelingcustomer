import unittest
from python.Matrix import Matrix


class TestMatrixMethods(unittest.TestCase):
    """
        unittest class for testing the various methods for matrices
    """
    def test_empty_list(self):
        """
            Test for when the user inputs no locations
        """
        distance_list = []
        matrix = Matrix(distance_list)

        result = matrix.matrix_solve()
        self.assertTrue(result == ([], 0))

    def test_single_list(self):
        """
            Test for when only a single location is given (the start location)
        """
        distance_list = [[0]]
        matrix = Matrix(distance_list)
        result = matrix.matrix_solve()
        self.assertTrue(result == ([0,0], 0))

    def test_double_list(self):
        """
            Test for user input of a single location excluding the start location
        """

        distance_list = [
            [0, 1],
            [1, 0]
        ]

        matrix = Matrix(distance_list)

        result = matrix.matrix_solve()

        self.assertTrue(result == ([0, 1, 0], 2))

    def test_tsp_order1(self):
        """
            Testing that the TSP Solution doesn't choose incorrectly
        """
        # Start, Chicago, Hofstra, Gary
        distance_list = [
            [0, 45187, 717, 43308],
            [44731, 0, 44906, 2461],
            [728, 45428, 0, 43550],
            [42990, 2497, 43164, 0]
        ]

        matrix = Matrix(distance_list)

        result = matrix.matrix_solve()

        # produces: Start, Gary, Chicago, Hofstra
        # Total Time: 91439

        self.assertTrue(result[1] == 91439)

        self.assertTrue(result[0][0] == 0)
        self.assertTrue(result[0][1] == 3)
        self.assertTrue(result[0][2] == 1)
        self.assertTrue(result[0][3] == 2)
        self.assertTrue(result[0][4] == 0)

    def test_tsp_order2(self):
        """
            Ensuring that the TSP Solution provides the same output regardless of the order of input
        """
        # Start, Gary, Hofstra, Chicago
        distance_list = [
            [0, 43308, 717, 45187],
            [42990, 0, 43164, 2497],
            [728, 43550, 0, 45428],
            [44731, 2461, 44906, 0],
        ]

        matrix = Matrix(distance_list)

        result = matrix.matrix_solve()

        # produces: Start, Gary, Chicago, Hofstra
        # Total Time: 91439

        self.assertTrue(result[1] == 91439)

        self.assertTrue(result[0][0] == 0)
        self.assertTrue(result[0][1] == 1)
        self.assertTrue(result[0][2] == 3)
        self.assertTrue(result[0][3] == 2)
        self.assertTrue(result[0][4] == 0)


    def test_tsp_with_data(self):
        """
            Testing the TSP Implementation with established dataset
            Data found here: https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html
        """

        distance_list = [
            [0, 29, 82, 46, 68, 52, 72, 42, 51, 55, 29, 74, 23, 72, 46]
            , [29, 0, 55, 46, 42, 43, 43, 23, 23, 31, 41, 51, 11, 52, 21]
            , [82, 55, 0, 68, 46, 55, 23, 43, 41, 29, 79, 21, 64, 31, 51]
            , [46, 46, 68, 0, 82, 15, 72, 31, 62, 42, 21, 51, 51, 43, 64]
            , [68, 42, 46, 82, 0, 74, 23, 52, 21, 46, 82, 58, 46, 65, 23]
            , [52, 43, 55, 15, 74, 0, 61, 23, 55, 31, 33, 37, 51, 29, 59]
            , [72, 43, 23, 72, 23, 61, 0, 42, 23, 31, 77, 37, 51, 46, 33]
            , [42, 23, 43, 31, 52, 23, 42, 0, 33, 15, 37, 33, 33, 31, 37]
            , [51, 23, 41, 62, 21, 55, 23, 33, 0, 29, 62, 46, 29, 51, 11]
            , [55, 31, 29, 42, 46, 31, 31, 15, 29, 0, 51, 21, 41, 23, 37]
            , [29, 41, 79, 21, 82, 33, 77, 37, 62, 51, 0, 65, 42, 59, 61]
            , [74, 51, 21, 51, 58, 37, 37, 33, 46, 21, 65, 0, 61, 11, 55]
            , [23, 11, 64, 51, 46, 51, 51, 33, 29, 41, 42, 61, 0, 62, 23]
            , [72, 52, 31, 43, 65, 29, 46, 31, 51, 23, 59, 11, 62, 0, 59]
            , [46, 21, 51, 64, 23, 59, 33, 37, 11, 37, 61, 55, 23, 59, 0]
        ]

        matrix = Matrix(distance_list)

        result = matrix.matrix_solve()

        self.assertTrue(result[0][0] == 0)
        self.assertTrue(result[0][1] == 12)
        self.assertTrue(result[0][2] == 1)
        self.assertTrue(result[0][3] == 14)
        self.assertTrue(result[0][4] == 8)
        self.assertTrue(result[0][5] == 4)
        self.assertTrue(result[0][6] == 6)
        self.assertTrue(result[0][7] == 2)
        self.assertTrue(result[0][8] == 11)
        self.assertTrue(result[0][9] == 13)
        self.assertTrue(result[0][10] == 9)
        self.assertTrue(result[0][11] == 7)
        self.assertTrue(result[0][12] == 5)
        self.assertTrue(result[0][13] == 3)
        self.assertTrue(result[0][14] == 10)
        self.assertTrue(result[0][15] == 0)


if __name__ == '__main__':
    unittest.main()