import csv
import pandas as pd

from utils.cleanser import replace_nan


def get_dataframe(file_name):
    ''' Return dataframe of file after reading it. '''
    fs = find_seperator(file_name)

    if len(fs) > 1:
        df = pd.read_fwf(file_name)
    else:
        df = pd.read_csv(file_name, sep=fs, low_memory=False)

    return df


def find_seperator(file_name):
    ''' Return seperator of file.'''
    with open(file_name, 'r') as myCsvfile:
        header = myCsvfile.readline()
        if header.find(";") != -1:
            return ";"
        if header.find(",") != -1:
            return ","
        if header.find("\t") != -1:
            return "\t"
        if header.find("|") != -1:
            return "|"

    # default delimiter (MS Office export)
    return "fwf"
