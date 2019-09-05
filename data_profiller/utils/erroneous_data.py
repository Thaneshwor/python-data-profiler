def get_erroneous_column(column_unique_data_type):
    '''Return the list of erroneous column having more then one datatype.'''

    erroneous_column = {}

    for k, v in column_unique_data_type.items():
        if (len(v) == 2 and 'None' not in v) or len(v) > 2:
            erroneous_column[k] = v
    return erroneous_column


# function to return erroneous row no. and  erroneous column information
def get_erroneous_information(df, column_datatype_line):

    erroneous_information = {}
    erroneous_row_no = []

    for k, v in column_datatype_line.items():
        # need to improve
        for k1, v1 in v.items():
            if(len(v1) < len(df)/2 and len(v1) > 0):
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
    print(erroneous_information)
    return erroneous_row_no, erroneous_information
