#!/usr/bin/env python3.10

import datetime as dt
import calendar


def get_day_name(day: str, month: str, year: str) -> str:
    """returns the day name of a particular date

    Args:
        day (str): day of month
        month (str): month name
        year (str): year name

    Returns:
        str: day name of a date
    """

    date_object = dt.datetime.strptime(f"{day}, {month}, {year}", "%d, %B, %Y")
    day_name = date_object.strftime("%A")
    return day_name


print()
print(" DAY NAME FETCHER ".center(50, "-"))
print("Get the day name of a particular date")

day = input("Enter day (1 - 31) -> ")
month = input("Enter month in full (January - December) -> ").capitalize()
year = input("Enter year -> ")

# list of full names of the 12 months
months = list(calendar.month_name)

if month not in months:
    print("Not a valid month")
    
else:
    
    # to get the number of days in month
    _, days_in_month = calendar.monthrange(int(year), months.index(month) + 1)
    
    # verifies that user does not input wrong day of month
    if int(day) > days_in_month:
        print(f"{month} has less than {day} days")
    
    # verifies that user does not input wrong day of month   
    elif int(day) <= days_in_month and int(day) != 0:
        day_name = get_day_name(day, month, year)
        
        if dt.datetime.now().year  <= int(year):
            print(f"{day} of {month}, {year} is a {day_name}")
            
        else:
            print(f"{day} of {month}, {year} was a {day_name}")


