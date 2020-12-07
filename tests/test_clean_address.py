import fuzzyexact
import pandas as pd
import string
import unittest


#setup test dataframe
my_dict1 = {'fname': ['eric', 'bob', 'john', 'phil', 'sarah', 'jen', 'jill', 'julie', 'jack', 'greg', 'jane'], 

           'lname': ['tomasi', 'johnson', 'smith', 'underhill', 'tango', 'whiskey', 'foxtrot', 'delta', 'benson', 'han', 'smol'],

           'address': ['150 right street? RM 205', 
                       '125 main road STE 5', 
                       '325 left _avenue', 
                       '255 test/close', 
                       '122 a BOULEVARDE', 
                       '556 meadow drive BLdG 1', 
                       '225 lark lane', 
                       '322 park place', 
                       '998 castle square_', 
                       '020889 country circuit', 
                       '123 high street ' + r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'], 

            'clean_address': ['150 right ST?', 
                       '125 main RD', 
                       '325 left _AVE', 
                       '255 test/CL', 
                       '122 a BLVD', 
                       '556 meadow DR', 
                       '225 lark LN', 
                       '322 park PL', 
                       '998 castle SQ_', 
                       '020889 country CCT', 
                       '123 high ST ' + r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'],

            'raw_road_types': ['street', 'road', 'avenue', 'close', 'BOULEVARDE', 'drive', 'lane', 'place', 'square', 'circuit', 'street'],

            'clean_road_types': ['ST', 'RD', 'AVE', 'CL', 'BLVD', 'DR', 'LN', 'PL', 'SQ', 'CCT', 'ST'], 

            'raw_buildings': ['MAIN BLDG 101', 'MAIN STE 1501', 'MAIN rM 501', None, None, None, None, None, None, None, None], 

            'clean_buildings': ['MAIN', 'MAIN', 'MAIN', None, None, None, None, None, None, None, None],

            'state': ['MA', 'NY', 'CA', 'TN', 'NY', 'FL', 'TX', 'TX', 'CA', 'CA', 'NY']}

df = pd.DataFrame(my_dict1)

#test dataframes
road = fuzzyexact.clean_address(df, 'raw_road_types')
bldg = fuzzyexact.clean_address(df, 'raw_buildings')
clean_addr = fuzzyexact.clean_address(df, 'address')


class TestCleanAddress(unittest.TestCase):
  '''test the clean_address function'''


  def test_address_shorten(self):
    '''ensure address road types are truncated properly (street->ST)'''
    self.assertTrue(df['clean_road_types'].equals(road['raw_road_types']))  

  def test_bldg(self):
    '''ensure building, suite and room numbers are stripped'''
    self.assertTrue(df['clean_buildings'].equals(bldg['raw_buildings'])) 

  def test_full(self):
    '''ensure full address column is truncated properly and removes building/suite/room numbers at once'''
    self.assertTrue(df['clean_address'].str.upper().equals(clean_addr['address']))

  def test_dtype(self):
    '''ensure that the object returned is a pandas dataframe'''
    self.assertTrue(isinstance(clean_addr, pd.DataFrame))

  #NEED TO FIX
  def test_records(self):
    '''ensure all rows are returned'''
    self.assertEqual(df.count(axis='columns').all(), clean_addr.count(axis='columns').all())


if __name__ == 'main':
 unittest.main()
