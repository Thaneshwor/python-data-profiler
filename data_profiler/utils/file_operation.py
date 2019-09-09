import csv
import json
import pandas as pd

from utils.logger import setup_logger
from utils.cleanser import replace_nan


error_logger = setup_logger('error_logger', 'error.log')


def get_dataframe(file_name):
    ''' Return dataframe of file after reading it. '''

    fs = find_seperator(file_name)

    if len(fs) > 1:
        df = pd.read_fwf(file_name)
    else:
        df = pd.read_csv(file_name, sep=fs, low_memory=False)

    df = replace_nan(df)

    return df


def find_seperator(file_name):
    ''' Return seperator of file.'''
    try:
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

    except Exception as e:
        print('error occurre---------------------', e)
        error_logger.error(e)

    return "fwf"


def get_dict_from_json(file_name):
    '''
    Return dictionary after loading data from json file.
    '''
    try:
        with open(file_name) as f:
            data = json.load(f)
        return data
    except Exception as e:
        print('Error Can not open ', file_name)
        error_logger.error(e)

    return {}
