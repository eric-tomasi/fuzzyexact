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
                       '556 meadow drive BLDG 1', 
                       '225 lark lane', 
                       '322 park place', 
                       '998 castle square_', 
                       '020889 country circuit', 
                       '123 high street ' + r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'], 

            'state': ['MA', 'NY', 'CA', 'TN', 'NY', 'FL', 'TX', 'TX', 'CA', 'CA', 'NY']}

df = pd.DataFrame(my_dict1)

no_punc = fuzzyexact.remove_punctuation(df, 'address')

class TestRemovePunctuation(unittest.TestCase):
	'''test the remove_punctuation function'''

	def test_punctuation(self):
		'''ensure no punctuation exists in column supplied'''
		self.assertFalse(no_punc['address'].str.contains(string.punctuation, regex=False).any())

	def test_dtype(self):
		'''ensure that the object returned is a pandas dataframe'''
		self.assertTrue(isinstance(no_punc, pd.DataFrame))

	def test_records(self):
		'''ensure all rows are returned'''
		self.assertEqual(df.count(axis='columns').all(), no_punc.count(axis='columns').all())


if __name__ == 'main':
	unittest.main()