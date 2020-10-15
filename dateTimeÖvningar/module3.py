#Write a Python program to get the day of the week for a specified date.

#Expected Output :

#The day of the week for 7/11/2016 is Monday.

#3b – gör en ”svensk” variant av detta!!!

from datetime import datetime

dag=(input("Give in the date dd/mm/yyyy : "))
d=int(dag[0])*10+int(dag[1])
m=int(dag[3])*10+int(dag[4])
y=int(dag[6])*1000+int(dag[7])*100+int(dag[8])*10+int(dag[9])
date=datetime(y,m,d)
print(f'The day of the week for {dag} is {date.strftime("%A")}')

dag=(input("Ange Datum yyyy/mm/dd : "))
d=int(dag[8])*10+int(dag[9])
m=int(dag[5])*10+int(dag[6])
y=int(dag[0])*1000+int(dag[1])*100+int(dag[2])*10+int(dag[3])
date=datetime(y,m,d)
if date.strftime("%w")=="0":
    print("veckodag på {dag} är söndag")
elif date.strftime("%w")=="1":
    print("veckodag på {dag} är mondag")
elif date.strftime("%w")=="2":
    print("veckodag på {dag} är tisdag")
elif date.strftime("%w")=="3":
    print("veckodag på {dag} är onsdag")
elif date.strftime("%w")=="4":
    print("veckodag på {dag} är torsdag")
elif date.strftime("%w")=="5":
    print("veckodag på {dag} är fredag")
elif date.strftime("%w")=="6":
    print(f"veckodag på {dag} är lördag")
