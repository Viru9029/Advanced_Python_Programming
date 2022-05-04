#13: Python program to convert Year/Month/Day to Day of Year.
import datetime
current_date = datetime.datetime.today()
current_year = current_date.year
start_year_date = datetime.datetime(current_year,1,1)
Date_of_year = str(current_date - start_year_date)
print("Date of year is : ", Date_of_year[0:7])
