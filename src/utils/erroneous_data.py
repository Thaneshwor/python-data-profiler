def get_erroneous_column(file_format, column_unique_data_type):
    '''Return the list of erroneous column having more then one datatype.'''

    erroneous_column = {}

    for column, datatypes in column_unique_data_type.items():
        if is_valid_column(column, file_format, datatypes):
            erroneous_column[column] = datatypes

    return erroneous_column


def is_valid_column(column, file_format, datatypes):
    '''
    Return True if column is errorneous else return False.
    '''

    try:
        if len(datatypes) == 1 and file_format[column] in datatypes:
            return False
        elif len(datatypes) == 2 and 'None' in datatypes and file_format[column] in datatypes:
            return False
        else:
            return True
    except KeyError as e:
        return False


# function to return erroneous row no. and  erroneous column information
def get_erroneous_information(file_format, column_datatype_line):

    erroneous_information = {}
    erroneous_row_no = []

    for k, v in column_datatype_line.items():
        # need to improve
        if k in file_format:
            actual_datatype = file_format[k]
        else:
            continue
        for k1, v1 in v.items():

            if k1 != actual_datatype and len(v1) > 0:
                if k not in erroneous_information:
                    erroneous_information[k] = {}
                    erroneous_information[k][k1] = []
                    erroneous_information[k][k1].extend(v1)

                else:
                    if k1 not in erroneous_information[k]:
                        erroneous_information[k][k1] = []
                        erroneous_information[k][k1].extend(v1)
                    else:
                        erroneous_information[k][k1].extend(v1)
                erroneous_row_no.extend(v1)

    return erroneous_row_no, erroneous_information
