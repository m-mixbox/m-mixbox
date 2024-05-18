
from math import nan
import pandas as pd
import os
import datetime
import pytz
from datetime import date as dt
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree
import time

def read_excel():


    df = pd.read_excel(r"C:\Users\MBSPL-Ayush\Desktop\tally.xlsx", engine='openpyxl')
    df.fillna('')
    #print(df)
# Create an empty list 
    df_list = [list(row) for row in df.values]
    #print(df_list)
# Output the converted list

    company_list = []
    amount_list = []
    date = []
    narration = []
    voucher_type = []
    voucher_number = []
    #for i in df_list:
        #print(i)
    for k in range(len(df_list)):
        
        company_name = []
        amount = []
        #print(df_list[k][0])
        if pd.isna(df_list[k][0]) :
            voucher_number.append('')
        else:
            voucher_number.append(str(df_list[k][0]))
        voucher_type.append(str(df_list[k][1]))
        date.append(df_list[k][2])
        narration.append(str(df_list[k][3]))
        j=5
        for i in range(4,len(df_list[k]),2):
            if not pd.isna(df_list[k][i]) or not pd.isna(df_list[k][j]):
                if pd.isna(df_list[k][i]) and not pd.isna(df_list[k][j]):
                    company_name.append(str(' '))
                else :
                    company_name.append(str(df_list[k][i]))
            if not pd.isna(df_list[k][j]):
                #print(df_list[k][j])
                amount.append(round(df_list[k][j],2))
            j+=2
        if sum(amount) == 0:
            company_list.append(company_name)
            amount_list.append(amount)
        else :
            company_list.append(company_name)
            amount_list.append(amount)
            #print('error in line no.')
            #print(k+2)
            #exit()
    #print(amount_list)
    return [company_list,amount_list,narration,date,voucher_type,voucher_number]

def convert_date_format(date):
    date_organised = []
    for i in date :
        #print(i)
        a = str(i).split(' ')[0]
        date_organised.append(a.replace('-','')) 
    return date_organised

def create_directory():
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        time = str(current_time.hour) + '-' + str(current_time.minute) +'-' + str(current_time.second)
        directory = str(dt.today())+ ' ' +time
        parent_dir = "D:/tally xml/"
        path = os.path.join(parent_dir, directory) 
        error = ''
        try:
            os.makedirs(path, exist_ok = True)
            print("Directory '%s' created successfully" % directory) 
            error = ''
        except OSError as error:
            print(error)
        return error,path

def xml_data():
                        [company_list,amount_list,narration,date_unorganised,voucher_type,voucher_number] = read_excel()
                        amount_list_count = []
                        filename_list = []
                        for i in range(len(amount_list)):
                            amount_list_count.append(len(amount_list[i]))
                        date = convert_date_format(date_unorganised)
                        
                        i=0
                        
                        z=0
                        #print(amount_list)
                        for i in range(len(amount_list)):
                            #print(i)
                            j=0
                            while(j+1 <= len(amount_list[i])):
                                    #print(j)
                                    xmldata = r"D:\xampp\htdocs\scripts\python codes\excel to xml to tally prime\ledger.xml" 
                                    tree2 = ElementTree()
                                    tree2.parse(xmldata) 
                                    ledger_entry_data = tree2.getroot()
                                    for ledger in ledger_entry_data.iter('ALLLEDGERENTRIES.LIST'):
                                        ledger.find('AMOUNT').text = str(amount_list[i][j])
                                        ledger.find('LEDGERNAME').text = str(company_list[i][j])
                                        if amount_list[i][j] > 0 :
                                            ledger.find('ISDEEMEDPOSITIVE').text = 'NO'
                                        else:
                                            ledger.find('ISDEEMEDPOSITIVE').text = 'YES'
                                        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
                                        directory = str(dt.today()) + ' '+ str(current_time.hour) + '-' + str(current_time.minute) +'-' + str(current_time.second)
                                        parent_dir = r"D:\xampp\htdocs\scripts\python codes\excel to xml to tally prime\xml data"
                                        path = os.path.join(parent_dir, directory) 
                                        error = ''
                                        try:
                                            os.makedirs(path, exist_ok = True)
                                            error = ''
                                            filename = path + '/'+str(z)+'.xml'
                                            filename_list.append(filename)
                                            tree2.write(filename,encoding="utf-8")
                                        except OSError as error:
                                            print(error)
                                        z+=1
                                    j+=1
                        return filename_list,[company_list,amount_list,narration,date_unorganised,voucher_type,voucher_number]

# get the start time
st = time.time()   

filename,[company_list,amount_list,narration,date_unorganised,voucher_type,voucher_number] = xml_data()
date_time = convert_date_format(date_unorganised)
xmldata = r"D:\xampp\htdocs\scripts\python codes\excel to xml to tally prime\request_data.xml" 
tree1 = ElementTree()
tree1.parse(xmldata) 
request_data = tree1.getroot()
xmldata = r"D:\xampp\htdocs\scripts\python codes\excel to xml to tally prime\tally_raw.xml" 
prstree = ElementTree()
prstree.parse(xmldata) 
root = prstree.getroot()

for import_data in root.iter('IMPORTDATA'):
    k=0
    for i in range(len(amount_list)):
        xmldata = r"D:\xampp\htdocs\scripts\python codes\excel to xml to tally prime\request_data.xml" 
        tree1 = ElementTree()
        tree1.parse(xmldata) 
        request_data = tree1.getroot()
        for voucher in request_data.iter('VOUCHER'):
            voucher.find('VOUCHERNUMBER').text = voucher_number[i]
            voucher.find('PARTYLEDGERNAME').text = company_list[i][0]
            voucher.find('NARRATION').text = narration[i]
            voucher.find('DATE').text = date_time[i]
            voucher.find('EFFECTIVEDATE').text = date_time[i]
            voucher.find('VOUCHERTYPENAME').text = voucher_type[i]
            voucher.attrib['VCHTYPE'] = voucher_type[i]
            for j in range(len(amount_list[i])):
                voucher.append(ET.parse(filename[k]).getroot())
                k+=1
        import_data.append(request_data)
error,path = create_directory()
filename = path + '/'+'data'+'.xml'
prstree.write(filename,encoding="utf-8")
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', round(elapsed_time,3), 'seconds')
