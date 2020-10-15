#Skriv ett program som loopar 10 gånger och lägger till 40 dagar till tidigare

#datum (börja med dagens) och skriver ut

from datetime import datetime, timedelta
dag = datetime.now()
for i in range(0,9):
    print(dag.strftime("%Y/%m/%d"))
    dag = dag + timedelta(40)
    

