
import pandas as pd
import json


path_of_json_file = r"D:\New folder\cgl gs\static gk\returns_11072024_R1_20AAUCA7296F1ZE_offline_others_0.json"
path_of_excel_file = r"D:\gstr1\data.xlsx"


import b2b
import b2cs
import nil
import b2b_line_items

with open(path_of_json_file) as f:
   raw_data = json.load(f)

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()




with pd.ExcelWriter(path_of_excel_file) as writer:
   
    # use to_excel function and specify the sheet_name and index 
    # to store the dataframe in specified sheet
    
    if 'b2b' in raw_data :
      df1 = b2b.df
      df2 = b2b_line_items.df
      df1.to_excel(writer, sheet_name="b2b", index=False)
      df2.to_excel(writer, sheet_name="b2b line items", index=False)
    if 'b2cs' in raw_data :
      df3 = b2cs.df
      df3.to_excel(writer, sheet_name="b2cs", index=False)
    if 'nil' in raw_data :
      df4 = nil.df
      df4.to_excel(writer, sheet_name="nil", index=False)