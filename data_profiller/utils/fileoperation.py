import csv
import pandas as pd
import itertools
import sys


def read_file(file_name):
    ''' Return dataframe of file after reading it. '''

    file_type = find_file_type(file_name)

    if file_type == 'csv':
        return pd.read_csv(file_name, delimiter=',', low_memory=False)
    elif file_type == 'fwf' or file_type == 'txt_fwf':
        return pd.read_fwf(file_name, low_memory=False)
    elif file_type == 'tsv':
        return pd.read_csv(file_name, sep='\t', low_memory=False)
    else:
        print('File Error Please provide csv, fwf, tsv or fwf(txt)')


def substring_after(s, delim):
    ''' Return file extension . '''
    return s.partition(delim)[2]


def generate_report(fields, column_unique_data_type):
    '''
    Generate report
    TODO: need to complete
    '''
    write_headers(fields)


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


def write_headers(fields):
    fields.insert(0, ['***************Fields***************')
    print('writing to file')

    with open('test_output.csv', 'w', newline='') as myfile:
        wr= csv.writer(myfile, delimiter='\n')
        wr.writerow(fields)
