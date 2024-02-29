from datetime import date

def weekday_of(date_string):
    return ((date.fromisoformat(date_string)).weekday() + 1)


print( weekday_of("1998-10-25") )
print( weekday_of("2001-01-01") )
print( weekday_of("1995-12-12") )