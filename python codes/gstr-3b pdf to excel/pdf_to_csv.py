

import code_main
import pandas as pd
#df = code_main.df
df1 = code_main.df1
df2 = code_main.df2
df3 = code_main.df3
df4 = code_main.df4
#gstin = code_main.gstin
#print(df1)
#print(df2)
#print(df3)
#print(df4)
excel_file_name = 'pandu.xlsx'
with open(excel_file_name, 'w') as fp:
    pass
with pd.ExcelWriter(excel_file_name) as writer:
   
    # use to_excel function and specify the sheet_name and index 
    # to store the dataframe in specified sheet
    #df.to_excel(writer, sheet_name="table1", index=False)
    df1.to_excel(writer, sheet_name="table1", index=False,startrow=8)
    df2.to_excel(writer, sheet_name="table2", index=False)
    df3.to_excel(writer, sheet_name="table3", index=False)
    df4.to_excel(writer, sheet_name="table4", index=False)