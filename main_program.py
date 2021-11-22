from datetime import timedelta
from datetime import datetime
from PATH_LIST import PATH_LIST
from s3_utilities import  is_path_exists
import math
import functools


def getPaths(months, raw_function = False):
    def getDates(start_date, end_date, path):
        newdate1 = datetime.strptime(start_date, "%d/%m/%Y")
        newdate2 = datetime.strptime(end_date, "%d/%m/%Y")
        if(newdate1 == newdate2):
            return
        
        day = newdate1.day
        month = newdate1.month
        year = newdate1.year
        new_path = f"{path}/{year}/{month}/{day}"

        if is_path_exists(new_path):
            print(new_path)
        else:
            return
        yesterday = newdate1 - timedelta(days = 1)
        yesterday = yesterday.strftime("%d/%m/%Y")
        getDates(yesterday, end_date, path)

    days = math.floor(months * 30.4167)
    start_date = datetime.today() - timedelta(days=days)
    start_date = start_date.strftime("%d/%m/%Y")
    if raw_function:
        return getDates
    return functools.partial(getDates, start_date, "01/01/2018")



get_date = getPaths(13)
for path in PATH_LIST:
    get_date(path)
