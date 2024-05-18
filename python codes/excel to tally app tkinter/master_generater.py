import pandas as pd
from math import nan
import pandas as pd
import os
import datetime
import pytz
from datetime import date as dt
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree

def read_excel(filepath):
    name = []
    parent = []
    df = pd.read_excel(filepath,engine='openpyxl')
    df.fillna('')
    df_list = [list(row) for row in df.values]
    for i in range(len(df_list)):
        name.append(str(df_list[i][0]))
        parent.append(str(df_list[i][1]))
    return [name,parent]

def xml_data(filepath):
    [name,parent] = read_excel(filepath=filepath)
    print('got the data from excel')
    #parent_directory = os.path.dirname(__file__)
    return [name,parent]

def generate_xml(filepath,save_filepath):
    [name,parent] = xml_data(filepath)
    #parent_directory = r'D:/res/master'
    xmldata = os.path.join(os.path.dirname(__file__),'master\\tallymessage.xml')
    tree1 = ElementTree()
    tree1.parse(xmldata) 
    #request_data = tree1.getroot()
    xmldata = os.path.join(os.path.dirname(__file__),'master\\tally_raw.xml')
    prstree = ElementTree()
    prstree.parse(xmldata) 
    root = prstree.getroot()
    print('iteration started')
    for import_data in root.iter('REQUESTDATA'):
        k=0
        print('inside requestdata')
        for i in range(len(name)):
            xmldata = os.path.join(os.path.dirname(__file__),'master\\tallymessage.xml')
            tree1 = ElementTree()
            tree1.parse(xmldata) 
            request_data = tree1.getroot()
            
            for ledger in request_data.iter('LEDGER'):
                ledger.attrib['NAME'] = name[i]
                ledger.find('ADDITIONALNAME').text = name[i]
                ledger.find('PARENT').text = parent[i]
                for name_list in ledger.iter('NAME.LIST'):
                    name_list.find('NAME').text = name[i]
                    k+=1
                    print(k)
            import_data.append(request_data)
            #ET.dump(request_data)
    #error,path = create_directory()
    print('iteration ended')
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    directory = str(dt.today())+ ' '+ str(current_time.hour) + '-' + str(current_time.minute) +'-' + str(current_time.second)
    #path = os.path.join(parent_directory,'generated')
    filename = save_filepath + '/'+' master '+directory+'.xml'
    prstree.write(filename,encoding="utf-8")
    return save_filepath + '/'+'master'+'.xml'
#parent_directory = os.path.dirname(__file__)
