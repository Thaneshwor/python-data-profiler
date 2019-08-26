import pandas as pd


# function to read file
def readFile(file_name):

    file_type = findFileType(file_name)

    if file_type == 'csv':
        return pd.read_csv(file_name, delimiter=',')
    elif file_type == 'fwf':
        return  pd.read_fwf(file_name)
    elif file_type == 'tsv':
        return pd.read_csv(file_name, sep='\t')
    elif file_type == 'txt_fwf':
        return pd.read_fwf(file_name)
    else:
        print('File Error Please provide csv, fwf, tsv or fwf(txt)')


    

def substring_after(s, delim):
    return s.partition(delim)[2]

# function which write df to file 
def writeToFile(name):
    print('writing to file........')



# function to find file type
def findFileType(file_name):
    ext = substring_after(file_name,'.')

    if ext == 'csv':

        df = pd.read_csv(file_name, delimiter=',')
        if len(df.columns) > 1:
            print('CSV File')
            return 'csv'
        else:
            print('Fixed Width File(CSV)')
            return 'fwf'
    elif ext == 'tsv':
        print('TSV File')
        return 'tsv'

    elif ext == 'txt':
        print('Fixed Width File(txt)')
        return 'txt_fwf'

    return 'file_error'
        