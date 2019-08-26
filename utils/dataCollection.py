from utils.dateUtils import is_date




# find and return column heading
def get_column_headings(data_frame):
    return list(data_frame.columns.values)


# count what datatype  are present and how many 
def count_data_type_in_each_column(column_data_type_information, heading):
    column_datatype_count = {}
    for column in heading:
        column_datatype_count[column] = {}
        for items in column_data_type_information[column]:
            
            if items not in column_datatype_count[column]:
                column_datatype_count[column][items] = 1
            else:
                column_datatype_count[column][items] = column_datatype_count[column][items]+1
    return column_datatype_count






# find and store column datatype at which line
# example dict = { year: {string:[1, 3, 4, 6], integer:[2, 5]}, value: { string:{4, 5, 6}}}
def getColumnDatatypesLine(df, heading):
    column_datatype_at_which_line = {}
    for index, row in df.iterrows():
        index = index+1
        for column in heading:
            list_heading = column
            dtype_cell = None
            x = None
            
            if list_heading in column_datatype_at_which_line:
                if row[list_heading] == 'NULL':
                    dtype_cell = None
                else:
                    try:
                        if is_date(row[list_heading]):
                            dtype_cell = 'date'
                        else:
                            dtype_cell = type(str(row[column]))
            
                            temp_var_float = str(row[column])
                            if '.' in temp_var_float:
                                dtype_cell = type(float(row[column]))
                            else:
                                dtype_cell = type(int(row[column]))
                    except:
                        x = ''
              
                if dtype_cell == int :
                    column_datatype_at_which_line[list_heading]['integer'].append(index)
                elif dtype_cell == float :
                    column_datatype_at_which_line[list_heading]['float'].append(index)
                elif dtype_cell == str:
                    column_datatype_at_which_line[list_heading]['string'].append(index)
                elif dtype_cell == 'date':
                    column_datatype_at_which_line[list_heading]['date'].append(index)
                elif dtype_cell == None :
                    column_datatype_at_which_line[list_heading]['None'].append(index)
                
            else:
                
                if row[list_heading] == 'NULL':
                    dtype_cell = None
                else:
                    try:
                        if is_date(row[list_heading]):
                            dtype_cell = 'date'
                        else:
                            dtype_cell = type(str(row[column]))
            
                            temp_var_float = str(row[column])
                            if '.' in temp_var_float:
                                dtype_cell = type(float(row[column]))
                            else:
                                dtype_cell = type(int(row[column]))

                    except:
                        x = ''
                column_datatype_at_which_line[list_heading] = {}
                column_datatype_at_which_line[list_heading]['integer'] = []
                column_datatype_at_which_line[list_heading]['float'] = []
                column_datatype_at_which_line[list_heading]['string'] = []
                column_datatype_at_which_line[list_heading]['date'] = []
                column_datatype_at_which_line[list_heading]['None'] =[]
                
                if dtype_cell == int:   
                    column_datatype_at_which_line[list_heading]['integer'].append(index)
           
                elif dtype_cell == float :  
                    column_datatype_at_which_line[list_heading]['float'].append(index)

                elif dtype_cell == str: 
                    column_datatype_at_which_line[list_heading]['string'].append(index)
                
                elif dtype_cell == 'date':
                    column_datatype_at_which_line[list_heading]['date'].append(index)

                elif dtype_cell == None:
                    column_datatype_at_which_line[list_heading]['None'].append(index)
   
    return column_datatype_at_which_line            








# function to return actual datatype of column
def getActualDatatypeOfColumns(column_datatype_at_which_line):

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
    
    column_data_type_information = {}

    for index, row in dataframe.iterrows():
        for column in headings:
            cell_data_type = None
        
            if column in column_data_type_information:
                if row[column] == 'NULL':
                    cell_data_type = None
                else:
                    try:
                        cell_data_type = type(str(row[column]))
                        cell_data_type = type(float(row[column]))
                        cell_data_type = type(int(row[column]))
                    except:
                        pass
                column_data_type_information[column].append(cell_data_type)
            else:
                if row[column] == 'NULL':
                    cell_data_type = None
                else:
                    try:
                        cell_data_type = type(str(row[column]))
                        cell_data_type = type(float(row[column]))
                        cell_data_type = type(int(row[column]))
                    except:
                        pass
                column_data_type_information[column] = []
                column_data_type_information[column].append(cell_data_type)
    return column_data_type_information
              





# return unique data type present in each column
def get_unique_data_type_in_each_column(df, heading):
    
    column_unique_data_type = {}
   
    datatype = {int:'integer',
            float:'float',
            str: 'string',
            None: 'None',
            'date': 'date'}

    for index, row in df.iterrows():
        for column in heading:
            list_heading = column
            dtype_cell = None
          
            if list_heading in column_unique_data_type:
                if row[column] == 'NULL':
                    dtype_cell = None
                else:
                    if is_date(row[list_heading]):
                        dtype_cell = 'date'
                        
                    else:
                        try:
                            dtype_cell = type(str(row[column]))
            
                            temp_var_float = str(row[column])
                            if '.' in temp_var_float:
                                dtype_cell = type(float(row[column]))
                            else:
                                dtype_cell = type(int(row[column]))
                        except:
                            pass
                
                if dtype_cell in datatype and datatype[dtype_cell] not in column_unique_data_type[list_heading]:
                    column_unique_data_type[list_heading].append(datatype[dtype_cell])
            
            else:
                if row[column] == 'NULL':
                    dtype_cell = None
                else:
                    if is_date(row[list_heading]):
                        dtype_cell = 'date'
                    else:
                        try:
                            dtype_cell = type(str(row[column]))
                          
                            temp_var_float = str(row[column])
                            if '.' in temp_var_float:
                                dtype_cell = type(float(row[column]))
                            else:
                                dtype_cell = type(int(row[column]))
                        except:
                            pass
                column_unique_data_type[list_heading] = []
                
                if dtype_cell in datatype and datatype[dtype_cell] not in column_unique_data_type[list_heading]:
                    column_unique_data_type[list_heading].append(datatype[dtype_cell])

    return column_unique_data_type
              

    
