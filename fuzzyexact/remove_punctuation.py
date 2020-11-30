import string

def remove_punctuation(df, column):
    '''strips punctuation from column in df and returns entire df'''
    df[column] = df[column].str.replace('[{}]'.format(string.punctuation), '')
    return df