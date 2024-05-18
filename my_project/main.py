import pandas as pd
import os

filepath = os.path.join(os.path.dirname(__file__),'stock_list.xlsx')
df = pd.read_excel(filepath,engine='openpyxl')
df_list = [list(row) for row in df.values]
ticker = []
company_name = []
for i in range(len(df_list)):
    ticker.append(df_list[i][1])
    company_name.append(df_list[i][2])
#print(company_name)
current_price = []
