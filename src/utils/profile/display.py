import sys

from datetime import datetime
from prettytable import PrettyTable
from utils.logger import setup_logger


message_logger = setup_logger("output_logger", "output.log", "message")
table_logger = setup_logger("table_logger", "output.log", "table")

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


def display_columns(headers):
    """
    Display columns header
    """

    index = 0
    pt = PrettyTable()
    pt.field_names = ["Index", "Column"]

    for column in headers:
        index = index + 1
        pt.add_row([index, column])

    print("\033[1;32;40m", dt_string, "[ INFO ] Columns headers \n")
    print(pt, "\n\n")
    message_logger.info("Columns headers")
    table_logger.info(pt)


def display_columns_datatype(column_unique_data_type):
    """
    Print all column and datatype available
    """

    index = 0
    pt = PrettyTable()
    pt.field_names = [
        "Index",
        "Column",
        "No. of datatype",
        "Datatype",
        "Nullable",
    ]

    for k, v in column_unique_data_type.items():
        index = index + 1
        temp_v = v
        is_nullable = False

        if "None" in v:
            temp_v.remove("None")
            is_nullable = True

        pt.add_row([index, k, len(v), temp_v, is_nullable])

    print(dt_string, "[ INFO ] Datatypes in each column \n ")
    print(pt, "\n\n")
    message_logger.info("Datatypes in each column ")
    table_logger.info(pt)


def display_columns_actual_datatype(actual_datatype_of_column, file_format):
    """
    Print Actual datatype of columns
    """

    index = 0
    pt = PrettyTable()
    if len(file_format) == 0:
        pt.field_names = ["Index", "Column", "Dominant Datatype"]

        for k, v in actual_datatype_of_column.items():
            index = index + 1
            pt.add_row([index, k, v])

    else:
        pt.field_names = [
            "Index",
            "Expected Columns",
            "Expected Datatypes",
            "Columns Present",
            "Dominant Datatype",
            "Match with format file",
        ]
        is_col_valid = "No"

        for k, v in file_format.items():
            index = index + 1
            if k in actual_datatype_of_column:
                is_col_valid = (
                    "Yes" if file_format[k] == actual_datatype_of_column[k] else "No"
                )

                pt.add_row(
                    [
                        index,
                        k,
                        file_format[k],
                        k,
                        actual_datatype_of_column[k],
                        is_col_valid,
                    ]
                )
            else:
                pt.add_row([index, k, file_format[k], "", "", is_col_valid])

        for k, v in actual_datatype_of_column.items():
            index = index + 1
            if k not in file_format:
                pt.add_row([index, "", "", k, actual_datatype_of_column[k], "No"])

    print(dt_string, "[ INFO ] Dominant datatype of column \n")
    print(pt, "\n\n")
    message_logger.info("Dominant datatype of column")
    table_logger.info(pt)


def display_erroneous_columns(erroneousColumn):
    """
    Print erroneous column and datatype available
    """

    if len(erroneousColumn) > 0:

        index = 0
        pt = PrettyTable()
        pt.field_names = ["Index", "Column", "Datatype"]

        for k, v in erroneousColumn.items():
            index = index + 1
            temp_v = v

            if "None" in temp_v:
                temp_v.remove("None")

            pt.add_row([index, k, temp_v])

        print(dt_string, "[ INFO ] Erroneous columns: Columns with more than one datatype \n")
        print(pt, "\n\n")
        message_logger.info("Erroneous columns: Columns with more than one datatype")
        table_logger.info(pt)
    else:
        message_logger.info("No erroneous columns present")


def display_erroneous_informatioin(erroneous_Column_Information):
    """
    Print erroneous columns and their datatypes and line number
    """

    if len(erroneous_Column_Information) > 0:

        index = 0
        pt = PrettyTable()
        pt.field_names = ["Index", "Column", "DataType", "Line"]

        for k, v in erroneous_Column_Information.items():
            for k1, v1 in v.items():
                index = index + 1
                if k1 != "None":
                    pt.add_row([index, k, k1, v1])

        print(dt_string, "[ INFO ] Erroneous columns and their line numbers \n")
        print(pt, "\n\n")
        message_logger.info("Erroneous columns and their line numbers")
        table_logger.info(pt)
