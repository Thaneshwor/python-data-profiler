import numpy as np


def replace_nan(dataframe):
    ''' Return the dataframe by replacing NaN with string NULL.  '''

    return dataframe.replace(np.nan, 'NULL', regex=True)
