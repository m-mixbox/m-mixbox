import random
import pandas as pd
date_list = []
amount_list = []
sum=0
while(sum<300000):
    i = 950 + random.randrange(11)*10
    amount_list.append(i)
    sum+=i
# Python3 code to demonstrate working of
# Random K dates in Range
# Using choices() + timedelta() + loop
from datetime import date, timedelta
from random import choices

# initializing dates ranges 
test_date1, test_date2 = date(2023, 4, 1), date(2024, 3, 31)

# printing dates 
#print("The original range : " + str(test_date1) + " " + str(test_date2))

# initializing K
K = len(amount_list)

res_dates = [test_date1]

# loop to get each date till end date
while test_date1 != test_date2:
	test_date1 += timedelta(days=1)
	res_dates.append(test_date1)

# random K dates from pack
date_list = choices(res_dates, k=K)

df= pd.DataFrame({'date':date_list,'amount':amount_list})
df.to_csv('abc.csv')
# printing 
#print("K random dates in range : " + str(res))
