"""
11:  Write a Python script to display the
a) Current date and time
b) Current year in full
c) Month of year full name
d) Weekday of the week
e) Day of year
f) Day of the month
g) Day of week in full name

"""
import datetime
current_date_time = datetime.datetime.today()
current_year = current_date_time.year
start_year_date = datetime.datetime(current_year,1,1)
print("a.Current Date and Time is : ",current_date_time)
print("b.Current year is : ", current_date_time.year)
print("c.Current month is :  ", current_date_time.strftime("%B"))
print("d.Weekday of the week is :  ", current_date_time.strftime("%w"))
differnce = str(current_date_time - start_year_date)
print("e.Day of year is :  ", differnce[0:7])
print("f.Day of the month :  ", current_date_time.strftime("%d"))
print("g.Day of week in full name :  ", current_date_time.strftime("%A"))