import xml.etree.ElementTree as ET
import pandas as pd 

# give the path where you saved the xml file 
# inside the quotes 
xmldata = r"D:\xampp\htdocs\scripts\excel to xml to tally prime\cashrec.xml" 
prstree = ET.parse(xmldata) 
root = prstree.getroot() 

#print(root) 

store_items = [] 
all_items = [] 
company_list = []
ledger = []
data = []

for req in root.iter('STATICVARIABLES'): 
	
	company_name = req.find('SVCURRENTCOMPANY').text.strip()
	company_list.append(company_name) 
	
print(company_list)

for req in root.iter('VOUCHER'): 
	
	v_type = req.find('VOUCHERTYPENAME').text.strip()
	date = req.find('DATE').text.strip() 
	party_name = req.find('PARTYLEDGERNAME').text.strip() 
	narration = req.find('NARRATION').text.strip() 
	
	for req in root.iter('ALLLEDGERENTRIES.LIST'):
		ledger_name = req.find('LEDGERNAME').text.strip() 
		amount = req.find('AMOUNT').text.strip() 
		ledger.append([ledger_name,amount])
		
	data.append([v_type,date,party_name,narration,ledger])
	
for i in data :
	for j in i:
		print(j)
	print(' ')
#for i in [elem.tag for elem in root.iter()]:
	#print(i)
#print()
#xmlToDf = pd.DataFrame(all_items, columns=[ 'SL No', 'ITEM_NUMBER', 'PRICE', 'QUANTITY', 'DISCOUNT']) 

#print(xmlToDf.to_string(index=False)) 
