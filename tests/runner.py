import unittest
import test_remove_punctuation
import test_clean_address

#set up test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

#add tests 
suite.addTests(loader.loadTestsFromModule(test_remove_punctuation))
suite.addTests(loader.loadTestsFromModule(test_clean_address))

#run suite
runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)