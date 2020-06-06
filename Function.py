import datetime
import unittest

# To find different between start and end dates
def diff_days(start, end):
    yy, mm, dd = tuple(map(int, start.split("-")))
    d1 = datetime.date(yy, mm, dd)
    yy, mm, dd = tuple(map(int, end.split("-")))
    d2 = datetime.date(yy, mm, dd)
    return (d2 - d1).days;


# To find NEXT_DATE of given date
def next_day(year, month, day):
    if (year % 400 == 0):
        leap_year = True
    elif (year % 100 == 0):
        leap_year = False
    elif (year % 4 == 0):
        leap_year = True
    else:
        leap_year = False
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        month_length = 28
        if leap_year:
            month_length = 29
    else:
        month_length = 30
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    d = datetime.date(year, month, day).strftime("%Y-%m-%d")
    return d



# Function Asked to submit
def Function(D):
    Input = sorted(D.items(), key=lambda x: x[0])
    D = [] #Making D as Empty List to store result
    for i in range(len(Input) - 1):
        start = Input[i][0]   #Comparing start_date and end_date
        end = Input[i + 1][0]
        diff = diff_days(start, end)   #difference between start and end date
        D.append(Input[i])
        if (diff == 1):
            continue
        x = (Input[i + 1][1] + (diff - 1) * (Input[i][1])) // (diff)    #Finding variable to solve equation
        prev_date = start
        for j in range(1, diff):
            year, month, day = tuple(map(int, prev_date.split('-')))
            prev_date = next_day(year, month, day)
            D.append((prev_date, (j) * (x) - (j - 1) * (Input[i][1])))

    D.append(Input[-1])
    return {x: y for x, y in D}


# {'2019-01-10':10,'2019-01-11':20,'2019-01-31':100}
# print({x:y for x,y in Function({'2019-01-10':10,'2019-01-11':20,'2019-01-13':10})})


