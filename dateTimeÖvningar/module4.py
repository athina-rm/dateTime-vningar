#Write a Python program to calculate what day of the week is 40 days from this moment

#Expected Output :

#Today = 8/20/2016 4:18:17 PM

#Thursday

from datetime import datetime, timedelta
idag = datetime.now()
print(f"Today = {idag}")
new_date = idag + timedelta(40)
print(new_date.strftime("%A"))
