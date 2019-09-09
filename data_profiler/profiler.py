import pandas as pd

from utils.file_operation import get_dataframe
from utils.file_operation import get_dict_from_json
from utils.data_collection import get_headers
from utils.profile.display import display_columns
from utils.data_collection import datatypes_in_column
from utils.data_collection import get_unique_data_type
from utils.data_collection import get_datatype_line_num
from utils.data_collection import count_data_type_in_each_column
from utils.data_collection import get_max_datatype
from utils.erroneous_data import get_erroneous_column
from utils.erroneous_data import get_erroneous_information
from utils.profile.display import display_erroneous_columns
from utils.profile.display import display_erroneous_informatioin
from utils.profile.display import display_columns_actual_datatype
from utils.profile.display import display_columns_datatype


def profileData(file_name, json_file_format):

    # collect data

    dataframe = get_dataframe(file_name)

    file_format = get_dict_from_json(json_file_format)

    column_headings = get_headers(dataframe)

    # get column datatype information
    column_datatype_information = datatypes_in_column(
        dataframe, column_headings)

    # return  how many datatype are present in which column
    column_datatype_count = count_data_type_in_each_column(
        column_datatype_information, column_headings)

    # return which datatype is present at which line
    column_datatype_line = get_datatype_line_num(dataframe, column_headings)

    # return column and their unique datatype
    column_unique_data_type = get_unique_data_type(
        dataframe, column_headings)
    # function to return actual datatype of column (need to imporove)
    max_datatype_of_column = get_max_datatype(
        column_datatype_line)
    # function to return erroneous column having more then one datatype
    erroneousColumn = get_erroneous_column(column_unique_data_type)
    # function to return erroneous row number and erroneous column row number
    erroneous_row_no, erroneous_Column_Information = get_erroneous_information(
        file_format, column_datatype_line)

    # print data profile
    display_data_profile(column_unique_data_type, column_headings,
                         max_datatype_of_column, erroneousColumn, erroneous_Column_Information, file_format)

    # generate_report(column_headings, column_unique_data_type)


# function to print profilled data
def display_data_profile(column_unique_data_type, column_headings, max_datatype_of_column, erroneousColumn, erroneous_Column_Information, file_format):
    print('************************************** DATA PROFILING **************************************')

    display_columns(column_headings)
    display_columns_datatype(
        column_unique_data_type)
    display_columns_actual_datatype(max_datatype_of_column, file_format)
    display_erroneous_columns(erroneousColumn)
    display_erroneous_informatioin(erroneous_Column_Information)
