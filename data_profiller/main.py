import sys

from profiler import profileData
# import pandas as pd

# entry point of program


def main(file_name):
    # datafile = 'new.csv'
    profileData(file_name)


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    json_file_format = str(sys.argv[2])

    main(file_name)
