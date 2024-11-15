from datetime import datetime, timedelta
import random
import functools

first = lambda x:x+15
second = lambda x, y: x*y
third = list(filter(lambda x: type(x)==int, [1.2, 1.3, 2, 4, 5]))
fourth = list(filter(lambda x: x%2==0, [1.2, 1.3, 2, 4, 5]))
fifth = list(filter(lambda x: x%2==1, [1.2, 1.3, 2, 4, 5]))
print(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().time)

# -----------------------------------------------
lst = [1,2,3,4,5,5,6,7,8,8,9]
even=len(list(filter(lambda x:x%2==0,lst)))
odd=len(list(filter(lambda x:x%2==1,lst)))
# -------------------------------------------------
lst = [[random.randint(0,1000) for i in range(10)] for i in range(10)]
maxnum = max(max(row) for row in lst)
maxnum = min(min(row) for row in lst)

# -------------------------------------------------
year = 2022
month = 12

if month == 12:
    last_day = datetime(year+1, 1, 1) - timedelta(days=1)
else:
    last_day = datetime(year, month+1, 1) - timedelta(days=1)

print(last_day)

for i in range(1, last_day.day + 1 ):
    print(datetime(year, month, i).strftime('%d-%m-%y %A'))