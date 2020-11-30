def clean_address(df, address_col):
    '''returns address in all CAPS, shortens road type (ST, RD, AVE), and strips out room/apt numbers'''

    #capitalize
    address = df[address_col].upper()

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
    
    #clean addresses
    df[address_col] = address