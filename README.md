# FuzzyExact
Perform fuzzy matching against two pandas dataframes with optional exact matches. 
<br/>
<br/>

## Requirements
Python 2.7 or higher<br/>
Pandas<br/>
FuzzyWuzzy<br/>
python-Levenshtein<br/>
<br/>
<br/>

## Installation
   ```pip install fuzzyexact```
<br/>
<br/>

## Usage
```import fuzzyexact```
<br/>
<br/>


### remove_punctuation
```python
fuzzyexact.remove_punctuation(df, 'column_name')
```

remove_punctuation is a helper function which strips all punctuation out of a column in pandas dataframe and returns the cleaned dataframe
<br/>

### clean_address
```python 
fuzzyexact.clean_address(df, 'address_column_name')
```

clean_address is a helper function which cleans an address column of a pandas dataframe by capitalizing, abbreviating road types (street>ST, road>RD), and stripping out building and suite numbers.
<br/>

### fuzzyexact
```python
fuzzyexact.fuzzyexact(df_left, df_right, id_col='Source_ID', key=('first_name', 'address'), block1='state', block2='last_name', threshold=80)
```

FuzzyExact leverages FuzzyWuzzy's process.extractOne ability, integrates it into pandas dataframes, and enables for up to two exact matches (or blocks) to significantly speed up performance of matching against large datasets. The function returns all rows from df_left along with the best match for each row in df_right. The id_col argument is an optional argument which allows the user to supply an id column from df_right to allow for easier lookups of matched records. The fuzzy match is performed against the key supplied by the user. block1 and block2 are optional arguments which specify exact matches between the two dataframes. The threshold is defaulted to 80, but can be altered by the user and will feed the cutoff to define a "good" match in FuzzyWuzzy's process.extractOne function. 
<br/>
<br/>

## Contact
Project: https://github.com/eric-tomasi/fuzzyexact <br/>
Email: etomasi2323@gmail.com
<br/>
<br/>

## Acknowledgments 

[FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy)
