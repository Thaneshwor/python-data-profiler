

from utils.date import is_date

datatype = {
    'integer': 'integer',
    'float': 'float',
    'string': 'string',
    None: 'None',
    'date': 'date'
}


def get_headers(dataframe):
    ''' Return the heading of columns present in dataframe. '''

    return list(dataframe.columns.values)


def count_data_type_in_each_column(col_data_type_info, heading):
    ''' Count and Return data types for each heading present in col_data_type_info . '''

    column_datatype_count = {}

    for column in heading:
        column_datatype_count[column] = {}

        for items in col_data_type_info[column]:
            column_datatype_count[column][items] = 1 if items not in column_datatype_count[
                column] else column_datatype_count[column][items]+1

    return column_datatype_count


def get_datatype_line_num(df, heading):
    '''
    Return dictionary which contains information about columns heading their datatypes and line numbers.

    Example :
        dict = { year: {string:[1, 3, 4, 6], integer:[
            2, 5]}, value: { string:{4, 5, 6}}}
    '''
    column_datatype_line_no = get_init_dictionary(heading)

    for index, row in df.iterrows():
        index = index+1
        for column in heading:
            column_datatype_line_no = store_line_no_of_datatype(
                row, column, index, column_datatype_line_no)

    return column_datatype_line_no

# store line no of datatype in each column


def store_line_no_of_datatype(row, column_heading, index, column_datatype_line_no):
    ''' Return dictionary (column_datatype_line_no) after adding line number of datatype in each column'''

    dtype_cell = None

    if column_heading in column_datatype_line_no:
        dtype_cell = get_datatype(row[column_heading])

        if dtype_cell in datatype:
            column_datatype_line_no[column_heading][datatype[dtype_cell]].append(
                index)

    else:
        dtype_cell = get_datatype(row[column_heading])

        if dtype_cell in datatype:
            column_datatype_line_no[column_heading][datatype[dtype_cell]].append(
                index)

    return column_datatype_line_no


# name need to be imporved

def get_init_dictionary(headings):
    ''' Return initialized dictionary for storing line number of of datatype  in each column of dataframe. '''

    column_datatype_line_no = {}

    for column_heading in headings:
        column_datatype_line_no[column_heading] = {}
        column_datatype_line_no[column_heading]['integer'] = []
        column_datatype_line_no[column_heading]['float'] = []
        column_datatype_line_no[column_heading]['string'] = []
        column_datatype_line_no[column_heading]['date'] = []
        column_datatype_line_no[column_heading]['None'] = []

    return column_datatype_line_no


def get_datatype(cell_value):
    ''' Return datatype of input parameter '''

    if cell_value == 'NULL':
        dtype_cell = None
    else:
        try:
            if is_date(cell_value):
                dtype_cell = 'date'
            else:
                dtype_cell = 'string'
                if '.' in cell_value:
                    dtype_cell = 'float'

                if int(cell_value):
                    dtype_cell = 'integer'

        except:
            pass
    return dtype_cell


# need to improve
def get_actual_datatype_of_columns(column_datatype_at_which_line):
    ''' Return actual datatype of column. '''
    column_datatype = {}

    for k, v in column_datatype_at_which_line.items():
        data_type = None
        no_of_time_data_type_occure = 0

        for k1, v1 in v.items():
            if(len(v1) > no_of_time_data_type_occure):
                data_type = k1
                no_of_time_data_type_occure = len(v1)
            column_datatype[k] = data_type

    return column_datatype


# return data types of column in  dicitonary
def datatypes_in_column(dataframe, headings):
    '''
    Return datatypes of column. 


    Result:
        {
            'year':['int', 'string'],
            'month':['int', 'string'],
        }
    TODO: Something in progress.
    '''
    result = {}

    for _, row in dataframe.iterrows():
        for column in headings:
            cell_data_type = get_datatype(row[column])

            if column in result:
                result[column].append(cell_data_type)
            else:
                result[column] = [cell_data_type]

    return result


def get_unique_data_type(df, heading):
    ''' Return unique datatype present in each column of dataframe. '''

    result = {}

    for _, row in df.iterrows():
        for column in heading:

            result = add_unique_datatype(
                row, column, result)

    return result


def add_unique_datatype(row, column_heading, column_unique_data_type):
    '''

    Return dicitionary after add datatype if previously not present in input dictionary (column_unique_data_type). 

    '''

    dtype_cell = None

    if column_heading in column_unique_data_type:
        dtype_cell = None if row[column_heading] == 'NULL' else get_datatype(
            row[column_heading])

        if dtype_cell in datatype and datatype[dtype_cell] not in column_unique_data_type[column_heading]:
            column_unique_data_type[column_heading].append(
                datatype[dtype_cell])

    else:
        dtype_cell = get_datatype(row[column_heading])
        column_unique_data_type[column_heading] = []

        if dtype_cell in datatype and datatype[dtype_cell] not in column_unique_data_type[column_heading]:
            column_unique_data_type[column_heading].append(
                datatype[dtype_cell])

    return column_unique_data_type
