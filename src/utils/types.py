''' Type utility functions. '''

import datetime


def is_date(date):
    ''' Return true if input parameter is date. '''

    formats = [
        "%Y%m%d",
        "%Y/%m/%d",
        "%m/%d/%Y",
        "%m/%d/%y",
        "%Y-%m-%d",
    ]

    for strptime_format in formats:
        try:
            datetime.datetime.strptime(date, strptime_format)
            return True
        except:
            pass

    return False


def is_date_time(date):
    ''' Return true if input parameter is date. '''

    formats = [
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S",
        "%Y/%m/%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%S.%f",
    ]

    for strptime_format in formats:
        try:
            datetime.datetime.strptime(date, strptime_format)
            return True
        except:
            pass

    return False


def is_float(val):
    ''' Return true if input parameter is of type float. '''

    if '.' not in str(val):
        return False

    try:
        float(val)

        return True
    except:

        return False


def is_int(val):
    ''' Return true if input parameter is of type integer. '''
    if '.' in str(val):
        return False

    try:
        return isinstance(int(float(val)), int)
    except:
        return False


def is_boolean(value):
    ''' Check if value is boolean. '''

    if value in [1, 0, '1', '0']:
        return True
    elif value.lower() in ['true', 'false', 'n', 'y', 'yes', 'no']:
        return True

    return False


def is_time(value):
    ''' Check if value is date. '''

    try:
        datetime.date(int(x[0:4]), int(x[5:7]), int(x[8:10]))
        return True
    except:
        return False
