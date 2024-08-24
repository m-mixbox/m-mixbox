import pandas as pd

df = pd.read_excel(r"D:\New folder\cgl gs\static gk\tally_test.xlsx", engine='openpyxl')
print(df)
df.fillna(' ',inplace=True)

print(df)