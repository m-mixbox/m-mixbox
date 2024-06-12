import pandas as pd
import numpy as np
import random

df = pd.read_excel(r"D:\New folder\cgl gs\convert.xlsx")
ass=df['POLICY_NO'].tolist()
unique = list(set(ass))
unique_np = np.array(ass)
#print(unique_np)
unique_values, counts = np.unique(unique_np, return_counts=True)

# Print the results
for value, count in zip(unique_values, counts):
    if(count>1):
        print(f"{value} occurs {count} times")
#for i in range(len(count_list)):
#    if(count_list.count > 2):

#fe_code_list = df['fe_code'].tolist()
#f= open('abc.txt',"w")
#f.write(sql)
#for i in range(8439):
#    f.write(fe_code_list[random.randrange(200)]+'\n')
    #print(fe_code_list[random.randrange(200)])
#f.close()
#print(df['fe_code'].tolist())