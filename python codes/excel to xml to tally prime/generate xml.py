from textwrap import indent
from numpy import fromstring
import pandas as pd
import os
import datetime
import pytz
from datetime import date
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree

def read_excel():


    df = pd.read_excel(r"D:\New folder\cgl gs\static gk\Ranchi Anupam kr. singh medicine.xlsx", engine='openpyxl')
    #print(df)
# Create an empty list 
    df_list = [list(row) for row in df.values]

# Output the converted list

    company_list = []
    amount_list = []
    date = []
    narration = []
    voucher_type = []
    #for i in df_list:
        #print(i)
    for k in range(len(df_list)):
        j=4
        company_name = []
        amount = []
        voucher_type.append(df_list[k][0])
        date.append(df_list[k][1])
        narration.append(df_list[k][2])
        for i in range(3,len(df_list[k]),2):
            if not pd.isna(df_list[k][i]):
                company_name.append(df_list[k][i])
            if not pd.isna(df_list[k][j]):
                #print(df_list[k][j])
                amount.append(df_list[k][j])
            j+=2
        if sum(amount) == 0:
            company_list.append(company_name)
            amount_list.append(amount)
        else :
            print('error in line no.')
            print(k+2)
            exit()
    #print(amount_list)
    return [company_list,amount_list,narration,date,voucher_type]

    #print(company_list)

def create_directory():
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        time = str(current_time.hour) + '-' + str(current_time.minute) +'-' + str(current_time.second)
        directory = str(date.today())+ ' ' +time
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

def convert_date_format(date):
    date_organised = []
    for i in date :
        a,b = str(i).split(' ')
        date_organised.append(a.replace('-','')) 
    return date_organised

def generate_xml():

    [company_list,amount_list,narration,date_unorganised,voucher_type] = read_excel()
    amount_list_count = []
    filename_list = []
    for i in range(len(amount_list)):
        amount_list_count.append(len(amount_list[i]))
    #print(amount_list_count)
    date = convert_date_format(date_unorganised)
    xmldata = r"D:\xampp\htdocs\scripts\excel to xml to tally prime\tally_raw.xml" 
    prstree = ElementTree()
    prstree.parse(xmldata) 
    root = prstree.getroot()

    if len(amount_list) >= 2:
        xmldata = r"D:\xampp\htdocs\scripts\excel to xml to tally prime\request_data.xml" 
        tree1 = ElementTree()
        tree1.parse(xmldata) 
        request_data = tree1.getroot()
        #ET.dump(request_data)
        for import_data in root.iter('IMPORTDATA'):
            for i in range(len(amount_list)):
                import_data.append(request_data)
            #import_data.append(request_data)
            #import_data.append(request_data)
            #import_data.append(request_data)
            #import_data.append(request_data)
        i=0
        z=0
        for req in root.iter('REQUESTDATA'):
                    #print(i)
                    for voucher in req.iter('VOUCHER'):

                        #print(narration[i])
                        xmldata = r"D:\xampp\htdocs\scripts\excel to xml to tally prime\ledger.xml" 
                        tree2 = ElementTree()
                        tree2.parse(xmldata) 
                        ledger_entry_data = tree2.getroot()
                        
                        j=0
                        for k in range(len(amount_list[i])):
                            #print(k)
                            voucher.append(ledger_entry_data)
                        for ledger in voucher.iter('ALLLEDGERENTRIES.LIST'):
                            #print(ledger)
                            #print(j)
                            if j+1 <= len(amount_list[i]) :
                                #print('here')
                                ledger.find('AMOUNT').text = str(amount_list[i][j])
                                ledger.find('LEDGERNAME').text = str(company_list[i][j])
                                #print(company_list[i][j])
                                j+=1
                                #voucher.append(ledger_entry_data)
                            else :
                                break
                            
                            current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
                            time = str(current_time.hour) + '-' + str(current_time.minute) +'-' + str(current_time.second)
                            directory = time
                            parent_dir = r"D:\xampp\htdocs\scripts\excel to xml to tally prime\xml data"
                            path = os.path.join(parent_dir, directory) 
                            error = ''
                            try:
                                os.makedirs(path, exist_ok = True)
                                #print("Directory '%s' created successfully" % directory) 
                                error = ''
                                filename = path + '/'+str(z)+'.xml'
                                filename_list.append(filename)
                                tree2.write(filename,encoding="utf-8")
                            except OSError as error:
                                print(error)
                            z+=1
                            #ET.dump(ledger)
                        #ET.dump(voucher)
                    i+=1
        #print(z)
        i=0
        for req in root.iter('REQUESTDATA'):
            for voucher in root.iter('VOUCHER'):
                voucher.find('NARRATION').text = narration[i]
                voucher.find('DATE').text = date[i]
                voucher.find('EFFECTIVEDATE').text = date[i]
                voucher.find('VOUCHERTYPENAME').text = voucher_type[i]
                voucher.attrib['VCHTYPE'] = voucher_type[i]
                i+=1
            ET.dump(req)

    #error,path = create_directory()
    #filename = path + '/'+'data'+'.xml'
  
    #with open(filename, "w") as f: 
        #f.write(prstree)  
    #prstree.write(filename,encoding="utf-8")
 
generate_xml()
