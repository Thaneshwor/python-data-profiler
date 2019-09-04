from prettytable import PrettyTable
import sys
import logging

logging.basicConfig(level=logging.DEBUG, filename='output.log',
                    format='%(asctime)s  \n\r%(message)s', datefmt='%Y/%m/%d %H:%M:%S')


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
    logging.info('All column headers in file')
    logging.info(pt)


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
    logging.info('Datatypes available in each column ')
    logging.info(pt)


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
    logging.info('Main datatype of column')
    logging.info(pt)


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
    logging.info('Erroneous columns present in file')
    logging.info(pt)


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
    logging.info('Erroneous columns and their line numbers')
    logging.info(pt)
