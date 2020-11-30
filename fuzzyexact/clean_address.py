def clean_address(df, address):
    '''returns address in all CAPS, shortens road type (ST, RD, AVE), and strips out room/apt numbers'''

    #capitalize
    df[address] = df[address].str.upper()

    #abbreviate road type
    df[address] = df[address].str.replace(r'\w*(?<!\w)(STREET)(?!\w)', 'ST')
    df[address] = df[address].str.replace(r'\w*(?<!\w)(ROAD)(?!\w)', 'RD')
    df[address] = df[address].str.replace(r'\w*(?<!\w)(AVENUE)(?!\w)', 'AVE')
    df[address] = df[address].str.replace(r'\w*(?<!\w)(CLOSE)(?!\w)', 'CL')
    df[address] = df[address].str.replace(r'\w*(?<!\w)(COURT)(?!\w)', 'CT')
    df[address] = df[address].str.replace(r'\w*(?<!\w)(BOULEVARDE)(?!\w)', 'BLVD')
    df[address] = df[address].str.replace(r'\w*(?<!\w)(DRIVE)(?!\w)', 'DR')
    df[address] = df[address].str.replace(r'\w*(?<!\w)(LANE)(?!\w)', 'LN')
    df[address] = df[address].str.replace(r'\w*(?<!\w)(PLACE)(?!\w)', 'PL')
    df[address] = df[address].str.replace(r'\w*(?<!\w)(SQUARE)(?!\w)', 'SQ')
    df[address] = df[address].str.replace(r'\w*(?<!\w)(CIRCUIT)(?!\w)', 'CCT')

    #strip room, apt, and building numbers
    df[address] = df[address].str.replace(r'STE[\s][\d]+$', '')
    df[address] = df[address].str.replace(r'RM[\s][\d]+$', '')
    df[address] = df[address].str.replace(r'BLDG[\s][\d]+$', '')
    
    return df