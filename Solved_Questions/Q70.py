#9: Print ten dates, each two a week apart, starting from today, in the form YYYY-MM-DD.
import datetime
today_date = datetime.date.today()
#print(today_date)
for i in range(0,20,2):
    dates = today_date + datetime.timedelta(weeks=i)
    print(dates)