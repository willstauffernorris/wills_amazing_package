import pandas as pd
import unittest
from package.my_mod import mega
from package.my_mod import list_to_series
from package.my_mod import date_breaker
from package.my_mod import Roadtrip

class TestModMethod(unittest.TestCase):

    def test_mega(self):
        '''
        This tests if the "mega" function is working properly.
        '''
        self.assertEqual(mega(2), 200)

    def test_list_to_series(self):
        '''
        This test makes sure that the type of a list is correct after going through the 'list_to_series' function
        '''
        self.assertEqual(type(list_to_series(['item a', 'item b', 'item c'])),
                         type(pd.Series(['item a', 'item b', 'item c']))
                         )

    #def test_date_breaker(self):
        #self.assertEqual(mega(2), 200)

   # def test_Roadtrip(self):
   #     self.assertEqual(mega(2), 200)

if __name__ == "__main__":
    unittest.main()
