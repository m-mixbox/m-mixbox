from importlib.resources import read_text
import pandas as pd
import string
# import xlsxwriter module 
import xlsxwriter 
 
# Workbook() takes one, non-optional, argument 
# which is the filename that we want to create. 
workbook = xlsxwriter.Workbook('sample.xlsx') 
 
# The workbook object is then used to add new 
# worksheet via the add_worksheet() method. 
worksheet = workbook.add_worksheet() 

f = open(r'python codes\26_as_txt_to_excel\AAICV0950D-2024.txt')

lst = f.readlines()
data = []
test_list = list(string.ascii_uppercase)
for i in lst :
    data.append(i.strip().split('^'))
for i in range(len(data)) :
    for j in range(len(data[i])) :
        text = str(test_list[j])+str(i)
        worksheet.write(text,data[i][j])
workbook.close() 
#lines = f.read()


#for i in lines :
    #print(i.split('^'))