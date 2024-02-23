#task №1
import datetime 
 
today = datetime.datetime.now()
fivedayago = datetime.datetime.now() - datetime.timedelta(days = +5)
print(fivedayago)

#task №2
import datetime

yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
today = datetime.datetime.now()
tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1)
print(yesterday)
print(today)
print(tomorrow)

#task №3
import datetime

datewithoutmicro = datetime.datetime.now() 
print(datewithoutmicro.strftime("%Y-%m-%d-%H-%M-%S")) #just formatting

#task №4

import datetime

date1 = datetime.datetime.now()
date2 = datetime.datetime(2020, 12, 9, 23, 11, 52, 10000)
diff = date1 - date2
print(diff.total_seconds())
#we can also use just print(date1 - date2).total_seconds()




