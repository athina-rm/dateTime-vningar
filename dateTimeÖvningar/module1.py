#. Skriv ett program som tar fram aktuell datum och tid och skriver ut

#Expected Output:

#Complete date: 2019-09-06 12:15:00

#Short Date: 2019-09-06
from datetime import datetime, timedelta
idag = datetime.now()
print(f"Complete date: {idag}")
print (f'Short date : {idag.strftime("%Y-%m-%d")}')
