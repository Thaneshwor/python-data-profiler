import pandas as pd

from utils.cleansing import replace_nan
from utils.fileoperation import read_file
from utils.datacollection import get_headings
from utils.profile.display import display_columns
from utils.datacollection import datatypes_in_column
from utils.datacollection import get_unique_data_type
from utils.datacollection import get_datatype_line_num
from utils.datacollection import count_data_type_in_each_column
from utils.datacollection import get_actual_datatype_of_columns
from utils.erroneousdata import get_erroneous_column
from utils.erroneousdata import get_erroneous_line_information
from utils.profile.display import display_erroneous_columns
from utils.profile.display import display_erroneous_informatioin
from utils.profile.display import display_columns_actual_datatype
from utils.profile.display import display_columns_datatype
from utils.fileoperation import write_to_file


def profileData(file_name):

    # collect data
    data_frame = read_file(file_name)
    # get column headings
    column_headings = get_headings(data_frame)
    # remove NaN values from data frame
    data_frame = replace_nan(data_frame)
    # get column datatype information
    column_datatype_information = datatypes_in_column(
        data_frame, column_headings)
    # return  how many datatype are present in which column
    column_datatype_count = count_data_type_in_each_column(
        column_datatype_information, column_headings)
    # return which datatype is present at which line
    column_datatype_line = get_datatype_line_num(data_frame, column_headings)
    # return column and their unique datatype
    column_unique_data_type = get_unique_data_type(
        data_frame, column_headings)
    # function to return actual datatype of column (need to imporove)
    actual_datatype_of_column = get_actual_datatype_of_columns(
        column_datatype_line)
    # function to return erroneous column having more then one datatype
    erroneousColumn = get_erroneous_column(column_unique_data_type)
    # function to return erroneous row number and erroneous column row number
    erroneous_row_no, erroneous_Column_Information = get_erroneous_line_information(
        data_frame, column_datatype_line)

    # print data profile
    display_data_profile(column_unique_data_type, column_headings,
                         actual_datatype_of_column, erroneousColumn, erroneous_Column_Information)


# function to print profilled data
def display_data_profile(column_unique_data_type, column_headings, actual_datatype_of_column, erroneousColumn, erroneous_Column_Information):
    print('************************************** DATA PROFILING **************************************')

    display_columns(column_headings)
    display_columns_datatype(
        column_unique_data_type, column_headings)
    display_columns_actual_datatype(actual_datatype_of_column)
    display_erroneous_columns(erroneousColumn)
    display_erroneous_informatioin(erroneous_Column_Information)

    write_to_file(column_headings, column_unique_data_type)
