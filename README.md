# Data Profiller

Generate reports from csv, tsv, fwf.

## For each column :
1. Print all column headers
2. Print all datatypes available in each column
3. Print expected columns, expected datatypes, columns presents, maximum datatype, isValid of each column
4. Print erroneous columns if present
5. Print erroneous columns row number 



## Installation
Download the source code by cloning the repository or by pressing 'Download ZIP' on this page. Install by navigating to the proper directory and running
~~~
python3 setup.py install
~~~


## How to run :
~~~
    python3 main.py $(path_to_file) 
    or
    python3 main.py $(path_to_file) $(path_to_format_file)

    Example:

    python3 ./src/main.py ./src/data/sample.csv
    or
    python3 ./src/main.py ./src/data/sample.csv ./src/data/sample-format.json
~~~


## Input CSV File
![](images/csv.jpg)

## Output

**Column headers**

![](images/column_headers.jpg)

**Columns and their available datatypes**

![](images/column_datatypes.jpg)

**Actual datatype of columns**

![](images/actual_datatypes.jpg)

**Erroneous column with datatypes**

![](images/err_column_datatypes.jpg)

**Erroneous column with row numbers and datatypes**

![](images/err_row_no.jpg)
