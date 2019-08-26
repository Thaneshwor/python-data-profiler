import re
import datetime
  
# check if input parameter is date
def is_date(date):
    # formats = [
    #     "%Y%m%d",
    #     "%Y/%m/%d",
    #     "%m/%d/%Y",
    #     "%m/%d/%y",
    #     "%Y-%m-%d",
    #     "%Y-%m-%dT%H:%M:%S%z",
    #     "%Y-%m-%dT%H:%M:%S",
    #     "%Y-%m-%dT%H:%M:%S.%f%z",
    #     "%Y-%m-%dT%H:%M:%S.%f",
    # ]


    if type(date) == str:
        return check_date_format(date)
        # for strptime_format in formats:
        #     try:
        #        return datetime.datetime.strptime(date, strptime_format)
        #     except ValueError:
        #       pass

    return False
    




# return true if input date format matches given date format
def check_date_format(date):
    
    x = re.search(r'(0[1-9]|[12]\d|3[01])\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s([12]\d{3})', date)
    if x :
        return True
    x = re.search(r'(0[1-9]|[12]\d|3[01])/(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\/([12]\d{3})', date)
    if x :
        return True
    x = re.search(r'(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/([12]\d{3})', date)
    if x :
        return True
    x = re.search(r'([1-9]|1[0-2])/([1-9]|[12]\d|3[01])/([12]\d{3})', date)
    if x :
        return True
    x = re.search(r'(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-([12]\d{3})', date)
    if x :
        return True
    
    x = re.search(r'(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-([12]\d{3})', date)
    if x :
        return True
    x = re.search(r'([1-9]|1[0-2])-([1-9]|[12]\d|3[01])-([12]\d{3})', date)
    if x :
        return True
    x = re.search(r'([12]\d{3})/(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])', date)
    if x :
        return True
    x = re.search(r'([12]\d{3})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])', date)
    if x :
        return True
    x = re.search(r'([12]\d{3})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])', date)
    if x :
        return True
    
    return False
