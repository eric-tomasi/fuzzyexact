def clean_address(df, address):
    '''returns address in all CAPS, shortens road type (ST, RD, AVE), and strips out room/apt numbers'''

    #capitalize
    df[address] = df[address].str.upper()

    #abbreviate road type
    df[address] = df[address].str.replace(r'\w*(?<!\w)(STREET)(?!\w)', 'ST').str.strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(ROAD)(?!\w)', 'RD').str.strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(AVENUE)(?!\w)', 'AVE').str.strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(CLOSE)(?!\w)', 'CL').str.strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(COURT)(?!\w)', 'CT').str.strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(BOULEVARDE)(?!\w)', 'BLVD').str.strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(DRIVE)(?!\w)', 'DR').str.strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(LANE)(?!\w)', 'LN').str.strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(PLACE)(?!\w)', 'PL').str.strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(SQUARE)(?!\w)', 'SQ').str.strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(CIRCUIT)(?!\w)', 'CCT').str.strip()

    #strip room, apt, and building numbers
    df[address] = df[address].str.replace(r'STE[\s][\d]+$', '').str.strip()
    df[address] = df[address].str.replace(r'RM[\s][\d]+$', '').str.strip()
    df[address] = df[address].str.replace(r'BLDG[\s][\d]+$', '').str.strip()
    
    return df