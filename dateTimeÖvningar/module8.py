#Write a program to get the difference between two dates in days.

#Expected Output :

#Difference in days: 2253

import datetime

date1=datetime.datetime.strptime(input("Ange datum 1: "),"%Y-%m-%d")
date2=datetime.datetime.strptime(input("Ange datum 2: "),"%Y-%m-%d")
diff=date1-date2
print ("Difference in days: ",diff.days)

