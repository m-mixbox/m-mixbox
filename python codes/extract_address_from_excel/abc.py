# import pandas lib as pd

import pandas as pd
import re

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel(r'python codes\extract_address_from_excel\assignment_data.xlsx')

address = []
pincode = []
for i in dataframe1['Address']:
    if not (pd.isna(i)):
        address.append(i)
for i in address:

    if type(i) == str :
            pincode.append([x for x in i.split(' ') if len(x)==6 and x.isdigit()])
with open('abc.txt', 'w') as f:
    for line in pincode:
        if(len(line)>0):
            f.write(f"{line[0]}\n")