#Write a program to get the number of days of the specified month and year.

import datetime

year=int(input("Ange år : "))
month=int(input("Ange månad : "))
date= datetime.datetime(year,month,1)
ndate=date+datetime.timedelta(31)
print (32-int(ndate.day))




