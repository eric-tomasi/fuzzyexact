import string

def remove_punctuation(df, column):
    for punctuation in string.punctuation:
        clean_column = str(df[column])
        clean_column = clean_column.replace(punctuation, '')
        df[column] = clean_column
    return df