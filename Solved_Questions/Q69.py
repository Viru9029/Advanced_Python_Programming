"""
8: Add week ( 7 days) and 12 hours to a given date
Given:
# 2020-03-22 10:00:00
given_date = datetime(2020, 3, 22, 10, 0, 0)
Expected output:
2020-03-29 22:00:00

"""
import datetime
set_date = datetime.datetime(2020,3,22,10,00,00)
additing_days = set_date + datetime.timedelta(days=7 , hours=10)
print("After adding 7 days and 10 hrs date and time is : ",additing_days)