print("MUHAMMAD SOHAIB - 18B-054-CS - SEC-A")
print("LAB NO: 02")

print("\nThis program will calculate the days between todays date and the given date.\n")
import datetime
date_today = datetime.date.today()
year = int(input("\nPlease enter the year  :"))
month = int(input("\nPlease enter the month :"))
day = int(input("\nPlease enter the day   :"))
date_user = datetime.date(year,month,day)
days = date_today - date_user
print("\n\nThe number of days between",date_today,"and",date_user,"is:",days.days,"days")
