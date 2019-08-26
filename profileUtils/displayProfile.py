from prettytable import PrettyTable


# function to print columns
def displayColumns(headers):
    index = 0
    x = PrettyTable()
    x.field_names = ['index','Available Column'];
    for column in headers:
        index = index+1
        x.add_row([index, column])
    print(x)



# funtion to print all column having and their datatypes
def displayAllDatatypesAvailableInColumns(column_unique_data_type, column_headings):
    index = 0
    print('*******************************************************************')
    print(' Columns  and their datatype Available:')
    x = PrettyTable()
    x.field_names = ['index','Column', 'no. of datatypes available', 'datatypes'];    
    for k, v in column_unique_data_type.items():
        index = index+1
        x.add_row([index, k, len(v), v])
    print(x)



# function to display actual datatype of columns
def displayActualDatatypeOfColumns(actual_datatype_of_column):
    print('********************************* Actual data type of column  **********************************')
    index = 0
    x = PrettyTable()
    x.field_names = ['Index','Column', 'Actual Datatype']
    for k, v in actual_datatype_of_column.items():
        index = index + 1
        x.add_row([index, k, v])
    print(x)



# function to display erroneousColumn
def displayErroneousColumn(erroneousColumn):
    print('********************************* Erroneous Columns  **********************************')
    index = 0
    x = PrettyTable()
    x.field_names = ['Index', 'Column', 'Datatype']
    
    for k, v in erroneousColumn.items():
        index = index + 1
        x.add_row([index, k, v ])
    
    print(x)


def displayErroneousInformatioin(erroneous_Column_Information):
    print('**********************************Erroneous Column Information*********************************')
    index = 0
    x = PrettyTable()
    x.field_names = ['Index','Column' ,'DataType', 'Error At Row Number']

    for k, v in  erroneous_Column_Information.items():
        for k1, v1 in v.items():
            index = index + 1
            x.add_row([index,k ,k1, v1])

    print(x)