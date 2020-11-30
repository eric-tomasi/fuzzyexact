import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='fuzzyexact',
      version='0.0.5',
      description='Perform fuzzy matching against two pandas dataframes with optional exact matches',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/eric-tomasi/fuzzyexact',
      author='Eric Tomasi',
      author_email='etomasi2323@gmail.com',
      keywords=['fuzzy', 'fuzzymatch', 'fuzzyexact', 'fuzzy block'],
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=['pandas', 'fuzzywuzzy']
      )