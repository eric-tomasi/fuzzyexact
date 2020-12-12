import fuzzyexact
import pandas as pd
import string
import unittest


class TestRemovePunctuation(unittest.TestCase):
	'''test the remove_punctuation function'''

	def setUp(self):
		'''set up test data frames'''
		self.my_dict1 = {'fname': ['eric', 'bob', 'john', 'phil', 'sarah', 'jen', 'jill', 'julie', 'jack', 'greg', 'jane'], 

               'lname': ['tomasi', 'johnson', 'smith', 'underhill', 'tango', 'whiskey', 'foxtrot', 'delta', 'benson', 'han', 'smol'],

               'address': ['150 right street? RM 205', 
                           '125 main road + STE 5', 
                           '325 left avenue_', 
                           '255 test/close', 
                           '122 a BOULEVARDE', 
                           '556 meadow drive BLdG 1', 
                           '225 lark "lane', 
                           '322 park place', 
                           '998 castle square', 
                           '020889 country _circuit', 
                           '123 high street ' + r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']}

		self.df = pd.DataFrame(self.my_dict1)
		self.df_test = self.df.copy()

		self.no_punc = fuzzyexact.remove_punctuation(self.df_test, 'address')

	def tearDown(self):
		self.my_dict1 = None
		self.df = None
		self.df_test = None
		self.no_punc = None

	def test_punctuation(self):
		'''ensure no punctuation exists in column supplied'''
		self.assertFalse(self.no_punc['address'].str.contains(string.punctuation, regex=False).any())

	def test_dtype(self):
		'''ensure that the object returned is a pandas dataframe'''
		self.assertTrue(isinstance(self.no_punc, pd.DataFrame))

	#NEED TO FIX
	def test_records(self):
		'''ensure all rows are returned'''
		self.assertEqual(self.df.count(axis='columns').all(), self.no_punc.count(axis='columns').all())