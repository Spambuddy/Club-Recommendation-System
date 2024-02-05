"""A3. Test cases for function club_functions.get_average_club_count.
"""

import unittest
import club_functions


class TestGetAverageClubCount(unittest.TestCase):
    """Test cases for function club_functions.get_average_club_count.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)

    def test_01_one_person_one_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
    
    def test_02_multiple_persons_multiple_clubs(self):
        param = club_functions.P2C
        actual = club_functions.get_average_club_count(param)
        expected = 1.6
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg = msg)
        
    
    def test_03_multiple_persons_no_clubs(self):
        param = {'Steve Yzerman': [], 'Margot Manuel': [], 'Rick Sanchez': []}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg = msg)
        
    def test_04_one_person_multiple_club(self):
        param = {'Claire Dunphy': ['Rocket Club', 'Science Club', 'Putnam']}
        actual = club_functions.get_average_club_count(param)
        expected = 3.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected)                 

if __name__ == '__main__':
    unittest.main(exit=False)
