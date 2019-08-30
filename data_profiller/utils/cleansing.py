import numpy as np
import pandas as pd


def replace_nan(dataframe):
    ''' Return the dataframe by replacing NaN with string NULL.  '''

    return dataframe.replace(np.nan, 'NULL', regex=True)


def remove_erroneous_column(dataframe, err_col_no):
    '''
    Remove erroneous row from dataframe

    TODO: need to complete
    '''
    print('removing erroneous column from dataframe')
