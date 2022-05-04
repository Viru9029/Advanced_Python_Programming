"""12: Python program to convert a string to datetime:
          'Jul 1 2016  2:43AM' into 2016-07-01 02:43:00
"""
import datetime
string_date = str("Jul 1 2016 2:43AM")
convert_string_to_datetime = datetime.datetime.strptime(string_date,"%b %d %Y %H:%M%p")
print(convert_string_to_datetime)