from fuzzywuzzy import process
import pandas as pd

def fuzzyexact(df_left, df_right, id_col=None, key=None,block1=None,block2=None,threshold=80):
    '''Fuzzy match function which takes df1 as input and returns fuzzy matched items from df2'''
    
    #create key
    if len(key) == 4:
        df_left['key'] = df_left[key[0]].str.replace(' ', '') + df_left[key[1]].str.replace(' ', '') + df_left[key[2]].str.replace(' ', '') + df_left[key[3]].str.replace(' ', '')
        df_right['key'] = df_right[key[0]].str.replace(' ', '') + df_right[key[1]].str.replace(' ', '') + df_right[key[2]].str.replace(' ', '') + df_right[key[3]].str.replace(' ', '')
    elif len(key) == 3:
        df_left['key'] = df_left[key[0]].str.replace(' ', '') + df_left[key[1]].str.replace(' ', '') + df_left[key[2]].str.replace(' ', '')
        df_right['key'] = df_right[key[0]].str.replace(' ', '') + df_right[key[1]].str.replace(' ', '') + df_right[key[2]].str.replace(' ', '')
    elif len(key) == 2:
        df_left['key'] = df_left[key[0]].str.replace(' ', '') + df_left[key[1]].str.replace(' ', '')
        df_right['key'] = df_right[key[0]].str.replace(' ', '') + df_right[key[1]].str.replace(' ', '')
    elif len(key) == 1:
         df_left['key'] = df_left[key[0]].str.replace(' ', '')
         df_right['key'] = df_right[key[0]].str.replace(' ', '')
       
    
    #run fuzzy matching
    matched = {'Match' :[], 'Score': []}

    for index, row in df_left.iterrows():
        
        if block1 is not None and block2 is not None:
            df_right_reduced = df_right[(df_right[block1] == row[block1]) & (df_right[block2] == row[block2])]
        elif block1 is not None and block2 is None:
            df_right_reduced = df_right[(df_right[block1] == row[block1])]
        elif block1 is None and block2 is None:
            df_right_reduced = df_right.copy()

        if len(df_right_reduced.index) > 0:
            match = process.extractOne(row['key'], df_right_reduced['key'], score_cutoff = threshold)
            if match is not None:
                matched['Match'].append(match[0])
                matched['Score'].append(match[1])
            else:
                matched['Match'].append('')
                matched['Score'].append('')
        else:
            matched['Match'].append('')
            matched['Score'].append('')
            
    matched = pd.DataFrame(matched)

    finl = pd.concat([df_left, matched], axis=1)
    
    #append ID column from df_right to allow for easy lookup
    if id_col is not None:
        ids = df_right.copy()
        ids = ids[['key', id_col]]
    
        finl = finl.merge(ids, left_on='Match', right_on='key', how='left', suffixes=('', '_y'))
        finl.drop(['key_y'], axis=1, inplace=True)
    
    return finl