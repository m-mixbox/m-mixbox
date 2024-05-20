from importlib.resources import read_text
import pandas as pd

df = pd.read_csv(r'python codes\26_as_txt_to_excel\AAICV0950D-2024.txt',sep="\t")

print(df)
