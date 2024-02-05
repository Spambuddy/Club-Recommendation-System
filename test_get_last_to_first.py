"""A3. Test cases for function club_functions.get_last_to_first.
"""

import unittest
import club_functions


class TestGetLastToFirst(unittest.TestCase):
    """Test cases for function club_functions.get_last_to_first.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_last_to_first(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_one_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_02_multiple_persons_multiple_friends_same_last(self):
        param = club_functions.P2F
        actual = club_functions.get_last_to_first(param)
        expected = {'Katsopolis': ['Jesse'],'Tanner': ['Danny R', 'Michelle','Stephanie J'],\
                    'Gladstone': ['Joey'],'Donaldson-Katsopolis': ['Rebecca'],'Gibbler': ['Kimmy'],\
                    'Tanner-Fuller': ['DJ']}
                    
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_03_multiple_person_one_friend_same_last(self):
        param = {'Clare Dunphy': ['Bob Dunphy'], 'Steve Dunphy': ['Clare Dunphy'],\
                 'Didier Dunphy': ['Joe Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Bob', 'Clare', 'Didier', 'Joe', 'Steve']}
        self.assertEqual(actual, expected)
        
    def test_04_multiple_person_no_friend(self):
        param = {'Clare Dunphy': [], 'Steve Dunphy': [],'Didier Dunphy': []}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Didier', 'Steve']}
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)
