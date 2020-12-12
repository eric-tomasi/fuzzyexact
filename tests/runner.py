import unittest
import test_remove_punctuation
import test_clean_address
import test_fuzzyexact

#set up test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

#add tests 
suite.addTests(loader.loadTestsFromModule(test_remove_punctuation))
suite.addTests(loader.loadTestsFromModule(test_clean_address))
suite.addTests(loader.loadTestsFromModule(test_fuzzyexact))

#run suite
runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)