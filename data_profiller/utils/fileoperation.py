import pandas as pd


def read_file(file_name):
    ''' Return dataframe of file after reading it. '''

    file_type = find_file_type(file_name)

    if file_type == 'csv':
        return pd.read_csv(file_name, delimiter=',')
    elif file_type == 'fwf' or file_type == 'txt_fwf':
        return pd.read_fwf(file_name)
    elif file_type == 'tsv':
        return pd.read_csv(file_name, sep='\t')
    else:
        print('File Error Please provide csv, fwf, tsv or fwf(txt)')


def substring_after(s, delim):
    ''' Return file extension . '''
    return s.partition(delim)[2]


# need to complete
def write_to_file(name):
    ''' write to csv file after removing error rows '''
    print('writing to file........')


# function to find file type
def find_file_type(file_name):
    ''' Return type of file. '''
    ext = substring_after(file_name, '.')

    if ext == 'csv':

        df = pd.read_csv(file_name, delimiter=',')
        if len(df.columns) > 1:
            print('CSV File')
            return 'csv'
        else:
            print('Fixed Width File(CSV)')
            return 'fwf'
    elif ext == 'tsv':
        print('TSV File')
        return 'tsv'

    elif ext == 'txt':
        print('Fixed Width File(txt)')
        return 'txt_fwf'

    return 'file_error'
