"""
10: Calculate number of days between two given dates
Given:
# 2020-02-25
date_1 = datetime(2020, 2, 25)
# 2020-09-17
date_2 = datetime(2020, 9, 17)
Expected output:
205 days

"""
import datetime
date_1 = datetime.date(2020,2,25)
date_2 = datetime.date(2020,9,17)
difference = str(date_2 - date_1)
print("Difference between above two dates is : ",difference[0:8])
