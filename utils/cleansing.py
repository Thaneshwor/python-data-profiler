import numpy as np
import pandas as pd 


# funtion to replace NaNs  with string 'NULL' in dataframe
def replace_NaN(dataframe):
    return dataframe.replace(np.nan, 'NULL', regex=True)



def remove_erroneous_column(dataframe, err_col_no):
    print('removing erroneous column from dataframe')
