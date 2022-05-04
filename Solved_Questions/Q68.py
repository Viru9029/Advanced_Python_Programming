#7: Subtract a week ( 7 days)  from a given date in Python
#2020-03-22 10:00:00
import datetime
set_date = datetime.datetime(2020,3,22,10,00,00)
subtract = set_date - datetime.timedelta(days=1)
print("After subtracting 7 days date and time is : ",subtract)