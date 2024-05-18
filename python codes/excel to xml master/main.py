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
    #parent_directory = os.path.dirname(__file__)
    return [name,parent]

def generate_xml(filepath):
    [name,parent] = xml_data(filepath)
    parent_directory = os.path.dirname(__file__)
    xmldata = os.path.join(parent_directory,"tallymessage.xml" )
    tree1 = ElementTree()
    tree1.parse(xmldata) 
    request_data = tree1.getroot()
    xmldata = os.path.join(parent_directory,"tally_raw.xml" )
    prstree = ElementTree()
    prstree.parse(xmldata) 
    root = prstree.getroot()

    for import_data in root.iter('REQUESTDATA'):
        k=0
        for i in range(len(name)):
            xmldata = os.path.join(parent_directory,"tallymessage.xml" )
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
            import_data.append(request_data)
    #error,path = create_directory()
    path = os.path.join(parent_directory,'generated')
    filename = path + '/'+'master'+'.xml'
    prstree.write(filename,encoding="utf-8")
#parent_directory = os.path.dirname(__file__)
generate_xml(r"D:\xampp\htdocs\scripts\python codes\excel to xml master\Master_Format.xlsx")