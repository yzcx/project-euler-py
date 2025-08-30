
# Project Euler problem 19

import datetime # I know I can use datetime library to handle calendar logic

date = datetime.date(1901, 1, 1)
sundays = 0

while date.year <= 2000:
    if date.weekday() == 6 and date.day == 1: # Checking if day is Sunday, and if day is first of the month
        sundays += 1


    date += datetime.timedelta(days=1) # Adding timedelta of 1 day to move to next day

print(sundays)
