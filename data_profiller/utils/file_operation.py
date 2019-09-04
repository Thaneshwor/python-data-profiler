import csv
import pandas as pd
import itertools
import sys


def get_dataframe(file_name):
    ''' Return dataframe of file after reading it. '''

    file_type = find_file_type(file_name)

    if file_type == 'csv':
        return pd.read_csv(file_name, delimiter=',', low_memory=False)
    elif file_type == 'fwf':
        return pd.read_fwf(file_name, low_memory=False)
    elif file_type == 'tsv':
        return pd.read_csv(file_name, sep='\t', low_memory=False)
    else:
        print('File Error Please provide csv, fwf, tsv or fwf(txt)')


def get_file_extension(s, delim):
    ''' Return file extension . '''
    return s.partition(delim)[2]


def find_file_type(file_name):
    ''' Return type of file. '''
    ext = get_file_extension(file_name, '.')

    if ext == 'csv':
        file_type = find_seperator(file_name)

        if file_type == ',':
            'csv'

        elif file_type == '\t':
            return 'tsv'
        else:
            print('Fixed Width File(CSV)')
            return 'fwf'
    elif ext == 'tsv' or ext == 'txt':
        print('TSV File')
        return 'tsv'

    return 'file_error'


def find_seperator(filename):
    with open(filename, 'r') as myCsvfile:
        header = myCsvfile.readline()
        if header.find(";") != -1:
            return ";"
        if header.find(",") != -1:
            return ","
        if header.find("\t") != -1:
            return "\t"
    # default delimiter (MS Office export)
    return ";"
