import fuzzyexact
import pandas as pd
import string
import unittest
import math


class TestFuzzyExact(unittest.TestCase):
  '''test the clean_address function'''

  def setUp(self):
    '''set up dataframes for testing'''

    self.my_dict1 = {'left_id': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],
            
               'fname': ['eric', 'bob', 'john', 'phil', 'sarah', 'jen', 'jill', 'julie', 'jack', 'greg', 'jane'], 

               'lname': ['tomasi', 'johnson', 'smith', 'underhill', 'tango', 'whiskey', 'foxtrot', 'delta', 'benson', 'han', 'smol'],

               'address': ['150 right street', 
                           '125 main road', 
                           '325 left avenue', 
                           '255 test close', 
                           '122 a BOULEVARDE', 
                           '556 meadow drive', 
                           '225 lark lane', 
                           '322 park place', 
                           '99829 castle park square', 
                           '020889 country circuit', 
                           '123 high street'], 

                'state': ['MA', 'NY', 'CA', 'TN', 'NY', 'FL', 'TX', 'TX', 'CA', 'CA', 'NY']}

    self.my_dict2 = {'fname': ['erica', 'bob', 'john', 'phillip', 'sarah', 'jen', 'jill', 'julia', 'jack', 'greg', 'jane'], 

               'lname': ['tomasi', 'johnsons', 'Williams', 'underhill', 'tango', 'whiskey', 'foxtrot', 'delta', 'benson', 'han', 'smol'],

               'address': ['150 right street', 
                           '125 main road', 
                           '325 lefty avenue', 
                           '256 test close', 
                           '29985 Sleepy Hollow Lane', 
                           '556 state street', 
                           '225 lark lane', 
                           '322 park place', 
                           '99829 castle park road', 
                           '20889 country circuit', 
                           '122 high street'], 

                'state': ['MA', 'NY', 'CA', 'TN', 'NY', 'FL', 'TX', 'TX', 'CA', 'NY', 'NY'], 
                'right_id': [1,2,3,4,5,6,7,8,9,10,11]}

    self.df_left = pd.DataFrame(self.my_dict1)
    self.df_right = pd.DataFrame(self.my_dict2)

    #test dataframes
    self.final = fuzzyexact.fuzzyexact(self.df_left, self.df_right, id_col='right_id', key=('fname', 'address'), block1='lname', block2='state')

  def test_matches(self):
    '''manually test each row that should match'''
    self.assertEqual(self.final['right_id'][0], 1)
    self.assertEqual(self.final['right_id'][3], 4)
    self.assertEqual(self.final['right_id'][6], 7)
    self.assertEqual(self.final['right_id'][7], 8)
    self.assertEqual(self.final['right_id'][8], 9)
    self.assertEqual(self.final['right_id'][10], 11)

  def test_non_matches(self):
    '''manually test rows that should not match'''
    self.assertTrue(math.isnan(self.final['right_id'][1]))
    self.assertTrue(math.isnan(self.final['right_id'][2]))
    self.assertTrue(math.isnan(self.final['right_id'][4]))
    self.assertTrue(math.isnan(self.final['right_id'][5]))
    self.assertTrue(math.isnan(self.final['right_id'][9]))


