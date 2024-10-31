#There is no penalty if you manage to solve the task some other way, but using the datetime.date API makes it very straight-forward. 
#The function will need to first convert the string to a datetime.date object and then return the weekday of the resulting datetime.date.
#Use the following template:

from datetime import date

def weekday_of(date_string):
    return date.weekday(date.fromisoformat(date_string)) + 1



# The following example illustrates how the solution may be used:
print( weekday_of("1998-10-25") )       # 7
print( weekday_of("2001-01-01") )       # 1
print( weekday_of("1995-12-12") )       # 2

