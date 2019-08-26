
# funtion to return list of erroneous column having more then one datatype
def getErroneousColumn(column_unique_data_type):
    index = 0
    erroneous_column = {}

   
    for k, v in column_unique_data_type.items():
        if(len(v)>1):
            erroneous_column[k] = v
    return  erroneous_column



# function to return erroneous row no. and  erroneous column information
def getErroneousLineInformation(df, column_datatype_line):
    erroneous_Column_Information = {}
    erroneous_row_no = []


    for k, v in column_datatype_line.items():
        # to improve
        for k1, v1 in v.items():
            if(len(v1)<len(df)/2 and len(v1)>0):
                if k not in erroneous_Column_Information:
                    erroneous_Column_Information[k] = {} 
                    erroneous_Column_Information[k][k1] = []
                    erroneous_Column_Information[k][k1].extend(v1)
                    
                else:
                    if k1 not in erroneous_Column_Information[k]:
                        erroneous_Column_Information[k][k1] = []
                        erroneous_Column_Information[k][k1].extend(v1)
                    else:
                        erroneous_Column_Information[k][k1].extend(v1)
                erroneous_row_no.extend(v1)
               
    return erroneous_row_no, erroneous_Column_Information
