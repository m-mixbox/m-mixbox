
import pandas as pd

#df = pd.read_json(r'D:\xampp\htdocs\scripts\json to csv\returns_15122023_R1_20AAUCA7296F1ZE_offline_others_0.json')

#print(df.to_string()) 
import json
import main

path_of_json_file = main.path_of_json_file

#path_of_json_file = r'D:\xampp\htdocs\scripts\json to csv\returns_26082023_R1_20AAGCT5841D1ZQ_offline_others_0.json'
with open(path_of_json_file) as f:
   raw_data = json.load(f)

gstin = raw_data['gstin']

b2cs_data = []
if 'b2cs'  in raw_data:
   b2cs_data = raw_data['b2cs']
else :
   exit()
fp = raw_data['fp']
fp1 = fp[:2]
fp2 = fp[2:]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July',
          'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
fp1 = months[int(fp1)-1]
fp = fp1+'-'+fp2
filling_period = []
supply_type = []
e_commerce_type = []
gst_rate = []
#these variables takes data from items
igst = []
cgst = []
sgst = []
tax_amount = []


for i in b2cs_data:
   supply_type.append(i['sply_ty'])
   e_commerce_type.append(i['typ'])
   gst_rate.append(i['rt'])
   cgst.append(i['camt'])
   sgst.append(i['samt'])
   tax_amount.append(i['txval'])
t_gstin = []
for x in range(len(b2cs_data)):
   t_gstin.append(gstin)
   filling_period.append(fp)
data =[t_gstin,filling_period,supply_type,e_commerce_type,gst_rate ,tax_amount,cgst,sgst]

dict = {}
header = ['TAXPAYER GSTIN','FILLING PERIOD', 'SUPPLY TYPE ','E-COMMERCE TYPE','GST RATE ','TAXABLE AMOUNT','CGST AMOUNT','SGST AMOUNT']
for i in range(len(header)) :
    dict[header[i]] = data[i]

df = pd.DataFrame(dict)
#print(df)