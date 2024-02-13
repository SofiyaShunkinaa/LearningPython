import datetime
import time

date1 = datetime.datetime.now()
date2 = time.time()  # временная метка даты и время
date3 = time.localtime()

print("Current date and time is: ", date1.strftime("%Y-%m-%d %H:%M:%S"))
print("Date: ", date1.strftime("%d/%m/%Y"))
print("Time: ", date1.strftime("%H:%M:%S"))

print("Current date and time is: ", date1.strftime("%d.%m.%Y %H:%M:%S"))
print("Date: ", date1.strftime("%d %B %Y"))
print("Time: ", date1.strftime("%H:%M"))
