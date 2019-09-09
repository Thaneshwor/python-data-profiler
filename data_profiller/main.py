import sys

from profiler import profileData
# import pandas as pd

# entry point of program


def main(file_name, json_file_format):
    # datafile = 'new.csv'
    profileData(file_name, json_file_format)


if __name__ == "__main__":
    try:
        file_name = str(sys.argv[1])
    except Exception as e:
        print('Please provide file path')

    try:
        json_file_format = str(sys.argv[2])
    except Exception as e:
        json_file_format = ''

    main(file_name, json_file_format)
