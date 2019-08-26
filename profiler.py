import pandas as pd

from utils.dataCollection import *
from utils.fileOperation import readFile  
from utils.erroneousData import getErroneousColumn
from profileUtils.displayProfile import displayColumns 
from utils.cleansing import replace_NaN
from utils.erroneousData import getErroneousLineInformation
from profileUtils.displayProfile import displayErroneousColumn
from profileUtils.displayProfile import displayErroneousInformatioin
from profileUtils.displayProfile import displayActualDatatypeOfColumns
from profileUtils.displayProfile import displayAllDatatypesAvailableInColumns



def profileData(file_name):

    # collect data 
    data_frame = readFile(file_name)
    # get column headings
    column_headings = get_column_headings(data_frame)
    # remove NaN values from data frame
    data_frame = replace_NaN(data_frame)
    # get column datatype information
    column_datatype_information = datatypes_in_column(data_frame, column_headings)
    # return  how many datatype are present in which column  
    column_datatype_count = count_data_type_in_each_column(column_datatype_information, column_headings)
    # return which datatype is present at which line
    column_datatype_line = getColumnDatatypesLine(data_frame, column_headings)
    # return column and their unique datatype
    column_unique_data_type = get_unique_data_type_in_each_column(data_frame, column_headings)
    # function to return actual datatype of column (need to imporove)
    actual_datatype_of_column = getActualDatatypeOfColumns(column_datatype_line)
    # function to return erroneous column having more then one datatype
    erroneousColumn = getErroneousColumn(column_unique_data_type)
    # function to return erroneous row number and erroneous column row number
    erroneous_row_no, erroneous_Column_Information = getErroneousLineInformation(data_frame, column_datatype_line)


    # print data profile 
    printDataProfile( column_unique_data_type, column_headings, actual_datatype_of_column, erroneousColumn, erroneous_Column_Information )
  

# function to print profilled data
def printDataProfile(column_unique_data_type, column_headings, actual_datatype_of_column, erroneousColumn, erroneous_Column_Information ):
    print('************************************** DATA PROFILING **************************************')
    displayColumns(column_headings)
    displayAllDatatypesAvailableInColumns(column_unique_data_type, column_headings)
    displayActualDatatypeOfColumns(actual_datatype_of_column)
    displayErroneousColumn(erroneousColumn)
    displayErroneousInformatioin(erroneous_Column_Information)