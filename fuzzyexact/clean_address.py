def clean_address(df, address):
    '''returns address in all CAPS, shortens road type (ST, RD, AVE), and strips out room/apt numbers'''

    #capitalize
    df[address] = df[address].str.upper()

    #abbreviate road type
    df[address] = df[address].str.replace(r'\w*(?<!\w)(STREET)(?!\w)', 'ST').strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(ROAD)(?!\w)', 'RD').strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(AVENUE)(?!\w)', 'AVE').strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(CLOSE)(?!\w)', 'CL').strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(COURT)(?!\w)', 'CT').strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(BOULEVARDE)(?!\w)', 'BLVD').strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(DRIVE)(?!\w)', 'DR').strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(LANE)(?!\w)', 'LN').strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(PLACE)(?!\w)', 'PL').strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(SQUARE)(?!\w)', 'SQ').strip()
    df[address] = df[address].str.replace(r'\w*(?<!\w)(CIRCUIT)(?!\w)', 'CCT').strip()

    #strip room, apt, and building numbers
    df[address] = df[address].str.replace(r'STE[\s][\d]+$', '').strip()
    df[address] = df[address].str.replace(r'RM[\s][\d]+$', '').strip()
    df[address] = df[address].str.replace(r'BLDG[\s][\d]+$', '').strip()
    
    return df