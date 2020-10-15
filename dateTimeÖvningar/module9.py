#Write a program in o check whether the given year, month and day are today or not.

#Test Data :

#Input the Day : 06

#Input the Month : 09

#Input the Year : 2019

#Expected Output :

#Detta är idag! Eller Detta är INTE idag

#Senast modifierad: onsdag, 16 september 2020, 13:31
from datetime import datetime

day=int(input("Input the day:"))
month=int(input("Input the Month:"))
year=int(input("Input the Year:"))
date=datetime(year,month,day)
today=datetime.now()
if date.date()==today.date():
    print("Detta är idag")
else:
    print("Detta är inte idag")
