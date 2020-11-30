import fuzzywuzzy
import pandas

def fuzzyexact(df_left, df_right, key=None,block1=None,block2=None,threshold=80):
    '''Fuzzy match function which takes df1 as input and returns fuzzy matched items from df2'''
    
    def clean_address(address):
        '''returns address in all CAPS, shortens road type (ST, RD, AVE), and strips out room/apt numbers'''
        #strip punctuation
        address = remove_punctuation(address)

        #capitalize
        address = address.upper()

        #abbreviate road type
        address = re.sub(r'\w*(?<!\w)(STREET)(?!\w)', 'ST', address)
        address = re.sub(r'\w*(?<!\w)(ROAD)(?!\w)', 'RD', address)
        address = re.sub(r'\w*(?<!\w)(AVENUE)(?!\w)', 'AVE', address)
        address = re.sub(r'\w*(?<!\w)(CLOSE)(?!\w)', 'CL', address)
        address = re.sub(r'\w*(?<!\w)(COURT)(?!\w)', 'CT', address)
        address = re.sub(r'\w*(?<!\w)(BOULEVARDE)(?!\w)', 'BLVD', address)
        address = re.sub(r'\w*(?<!\w)(DRIVE)(?!\w)', 'DR', address)
        address = re.sub(r'\w*(?<!\w)(LANE)(?!\w)', 'LN', address)
        address = re.sub(r'\w*(?<!\w)(PLACE)(?!\w)', 'PL', address)
        address = re.sub(r'\w*(?<!\w)(SQUARE)(?!\w)', 'SQ', address)
        address = re.sub(r'\w*(?<!\w)(CIRCUIT)(?!\w)', 'CCT', address)

        #strip room, apt, and building numbers
        address = re.sub(r'STE[\s][\d]+$', '', address).strip()
        address = re.sub(r'RM[\s][\d]+$', '', address).strip()
        address = re.sub(r'BLDG[\s][\d]+$', '', address).strip()

        return address
    
    #clean addresses
    df1.iloc[:,2] = df1.iloc[:,2].apply(clean_address)
    
    #create key
    if len(key) == 4:
        df1['key'] = df1[key[0]].str.replace(' ', '') + df1[key[1]].str.replace(' ', '') + df1[key[2]].str.replace(' ', '') + df1[key[3]].str.replace(' ', '')
        df2['key'] = df2[key[0]].str.replace(' ', '') + df2[key[1]].str.replace(' ', '') + df2[key[2]].str.replace(' ', '') + df2[key[3]].str.replace(' ', '')
    elif len(key) == 3:
        df1['key'] = df1[key[0]].str.replace(' ', '') + df1[key[1]].str.replace(' ', '') + df1[key[2]].str.replace(' ', '')
        df2['key'] = df2[key[0]].str.replace(' ', '') + df2[key[1]].str.replace(' ', '') + df2[key[2]].str.replace(' ', '')
    elif len(key) == 2:
        df1['key'] = df1[key[0]].str.replace(' ', '') + df1[key[1]].str.replace(' ', '')
        df2['key'] = df2[key[0]].str.replace(' ', '') + df2[key[1]].str.replace(' ', '')
        
    #clean key
    df1['key'] = df1['key'].apply(remove_punctuation)
    df2['key'] = df2['key'].apply(remove_punctuation)
        
    
    #run fuzzy matching
    matched = {'Match' :[], 'Score': []}

    for  index, row in df1.iterrows():
        
        if block1 is not None and block2 is not None:
            df2_reduced = df2[(df2[block1] == row[block1]) & (df2[block2] == row[block2])]
        elif block1 is not None and block2 is None:
            df2_reduced = df2[(df2[block1] == row[block1])]
        elif block1 is None and block2 is None:
            df2_reduced = df2.copy()

        if len(df2_reduced.index) > 0:
            match = process.extractOne(row['key'], df2_reduced['key'], score_cutoff = threshold)
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

    temp = pd.concat([df1, matched], axis=1)
    
    
    #grab CID from df2
    cids = df2.copy()
    cids = cids[['key', 'ID']]
    
    finl = temp.merge(cids, left_on='Match', right_on='key', how='left', suffixes=('', '_y'))
    finl.drop(['key_y'], axis=1, inplace=True)
    
    return finl