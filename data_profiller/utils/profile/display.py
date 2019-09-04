import sys

from prettytable import PrettyTable
from utils.logger import setup_logger


output_logger = setup_logger('output_logger', 'output.log')


def display_columns(headers):
    '''
    Display columns header

    '''
    index = 0
    pt = PrettyTable()
    pt.field_names = ['index', 'Available Column']
    for column in headers:
        index = index+1
        pt.add_row([index, column])
    print(pt)
    output_logger.info('Columns header in file')
    output_logger.info(pt)


def display_columns_datatype(column_unique_data_type):
    '''
    Print all column and datatype available
    '''
    index = 0
    print('*******************************************************************')
    print(' Columns  and their datatype Available:')
    pt = PrettyTable()
    pt.field_names = ['index', 'Column',
                      'no. of datatypes available', 'datatypes']
    for k, v in column_unique_data_type.items():
        index = index+1
        pt.add_row([index, k, len(v), v])
    print(pt)
    output_logger.info('Datatypes available in each column ')
    output_logger.info(pt)


def display_columns_actual_datatype(actual_datatype_of_column):
    '''
    Print Actual datatype of columns
    '''
    print('********************************* Actual data type of column  **********************************')
    index = 0
    pt = PrettyTable()
    pt.field_names = ['Index', 'Column', 'Actual Datatype']
    for k, v in actual_datatype_of_column.items():
        index = index + 1
        pt.add_row([index, k, v])
    print(pt)
    output_logger.info('Main datatype of column')
    output_logger.info(pt)


def display_erroneous_columns(erroneousColumn):
    '''
    Print erroneous column and datatype available
    '''
    print('********************************* Erroneous Columns  **********************************')
    index = 0
    pt = PrettyTable()
    pt.field_names = ['Index', 'Column', 'Available Datatypes']

    for k, v in erroneousColumn.items():
        index = index + 1
        pt.add_row([index, k, v])
    print(pt)
    output_logger.info('Erroneous columns present in file')
    output_logger.info(pt)


def display_erroneous_informatioin(erroneous_Column_Information):
    '''
    Print erroneous columns and their datatypes and line number

    '''
    print('**********************************Erroneous Column Information*********************************')
    index = 0
    pt = PrettyTable()
    pt.field_names = ['Index', 'Column', 'DataType', 'Error At Row Number']

    for k, v in erroneous_Column_Information.items():
        for k1, v1 in v.items():
            index = index + 1
            pt.add_row([index, k, k1, v1])
    print(pt)
    output_logger.info('Erroneous columns and their line numbers')
    output_logger.info(pt)
