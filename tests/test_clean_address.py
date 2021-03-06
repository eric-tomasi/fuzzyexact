import fuzzyexact
import pandas as pd
import string
import unittest


class TestCleanAddress(unittest.TestCase):
  '''test the clean_address function'''

  def setUp(self):
    '''set up dataframes for testing'''

    self.my_dict1 = {'fname': ['eric', 'bob', 'john', 'phil', 'sarah', 'jen', 'jill', 'julie', 'jack', 'greg', 'jane'], 

               'lname': ['tomasi', 'johnson', 'smith', 'underhill', 'tango', 'whiskey', 'foxtrot', 'delta', 'benson', 'han', 'smol'],

               'address': ['150 right street? RM 205', 
                           '125 main road STE 5', 
                           '325 left avenue', 
                           '255 test/close', 
                           '122 a BOULEVARDE', 
                           '556 meadow drive BLdG 1', 
                           '225 lark lane', 
                           '322 park place', 
                           '998 castle square', 
                           '020889 country circuit', 
                           '123 high street ' + r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'], 

                'clean_address': ['150 RIGHT ST?', 
                           '125 MAIN RD', 
                           '325 LEFT AVE', 
                           '255 TEST/CL', 
                           '122 A BLVD', 
                           '556 MEADOW DR', 
                           '225 LARK LN', 
                           '322 PARK PL', 
                           '998 CASTLE SQ', 
                           '020889 COUNTRY CCT', 
                           '123 HIGH ST ' + r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'],

                'raw_road_types': ['street', 'road', 'avenue', 'close', 'BOULEVARDE', 'drive', 'lane', 'place', 'square', 'circuit', 'street'],

                'clean_road_types': ['ST', 'RD', 'AVE', 'CL', 'BLVD', 'DR', 'LN', 'PL', 'SQ', 'CCT', 'ST'], 

                'raw_buildings': ['MAIN BLDG 101', 'MAIN STE 1501', 'MAIN rM 501', None, None, None, None, None, None, None, None], 

                'clean_buildings': ['MAIN', 'MAIN', 'MAIN', None, None, None, None, None, None, None, None],

                'state': ['MA', 'NY', 'CA', 'TN', 'NY', 'FL', 'TX', 'TX', 'CA', 'CA', 'NY']}

    self.df = pd.DataFrame(self.my_dict1)
    self.df_test = self.df.copy()

    #test dataframes
    self.road = fuzzyexact.clean_address(self.df_test, 'raw_road_types')
    self.bldg = fuzzyexact.clean_address(self.df_test, 'raw_buildings')
    self.clean_addr = fuzzyexact.clean_address(self.df_test, 'address')

  def tearDown(self):
    '''delete all dataframes'''
    self.df = None
    self.df_test = None
    self.road = None
    self.bldg = None
    self.clean_addr = None

  def test_address_shorten(self):
    '''ensure address road types are truncated properly (street->ST)'''
    self.assertTrue(self.df['clean_road_types'].equals(self.road['raw_road_types']))  

  def test_bldg(self):
    '''ensure building, suite and room numbers are stripped'''
    self.assertTrue(self.df['clean_buildings'].equals(self.bldg['raw_buildings'])) 

  def test_full_addr(self):
    '''ensure full address column is truncated properly and removes building/suite/room numbers at once'''
    self.assertTrue(self.df['clean_address'].equals(self.clean_addr['address']))

  def test_dtype(self):
    '''ensure that the object returned is a pandas dataframe'''
    self.assertTrue(isinstance(self.clean_addr, pd.DataFrame))