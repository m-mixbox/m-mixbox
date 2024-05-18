

import fitz
import pandas as pd 
import file_path
file_path_of_pdf = file_path.file_path_of_pdf
doc = fitz.open(file_path_of_pdf)
words=''
for i in doc :
    words+=i.get_text()
#print(words)
#page1 = doc[0]
#page2 = doc[1]
#page3 = doc[2]
#words = page1.get_text()+page2.get_text()+page3.get_text()
data = []



data = words.split('\n')
details_table = []
header = []
table_1 = []
table_2 = []
table_3 = []
table_4 = []
table_5 = []
table_6 = []
date = []
abc = '2(c). ARN'

j= data.index(abc)-12

sub = "3.1.1 Details of Supplies notified under section 9(5) of the CGST Act, 2017 and corresponding provisions in IGST/UTGST/SGST Acts"
check = []
check = ["3.1 Details of Outward supplies and inward supplies liable to reverse charge","3.2 Out of supplies made in 3.1 (a) above, details of inter-state supplies made","4.  Eligible ITC","5  Values of exempt, nil-rated and non-GST inward supplies","5.1 Interest and Late fee for previous tax period","6.1 Payment of tax","Breakup of tax liability declared (for interest computation)"]
header = ["3.1 Details of Outward supplies and inward supplies liable to reverse charge","4. Eligible ITC","5.1 Interest and Late fee for previous tax period","6.1 Payment of tax"]

# getting elements in between
if sub in data :
    idx1 = data.index(check[0])
    idx2 = data.index(sub)
else :
    idx1 = data.index(check[0])
    idx2 = data.index(check[1])

for idx in range(idx1+1 , idx2):
    table_1.append( data[idx])
#print(table_1)
idx3 = data.index(check[2])
idx4 = data.index(check[3])
idx5 = data.index(check[4])
idx6 = data.index(check[5])
idx7 = data.index(check[6])

for idx in range(idx3 +1, idx4):
    table_2.append( data[idx])

for idx in range(idx5 +1, idx6):
    table_3.append( data[idx])

for idx in range(idx6 +1, idx7):
    table_4.append( data[idx])


#gstin = details_table[1]
table_1_heading_raw = []
table_2_heading_raw = []
table_3_heading_raw = []
table_4_heading_raw = []


for i in range(10):
    table_1_heading_raw.append(table_1[i])
for i in range(5):
    table_2_heading_raw.append(table_2[i])
for i in range(5):
    table_3_heading_raw.append(table_3[i])
for i in range(17):
    table_4_heading_raw.append(table_4[i])


table_1_data = []
for i in table_1:
    if i.isdigit() or i.replace('.', '', 1).isdigit()  or i == '-':
        table_1_data.append(i)
#print(len(table_1_data))
#table_1_data = table_1[12:17]+table_1[18:23]+table_1[24:29]+table_1[30:35]+table_1[36:41]
table_1_heading = ["Nature of Supplies","Total taxable value","Integrated tax","Central tax","State/UT tax","Cess"]
field_table_1 = ["(a) Outward taxable supplies (other than zero rated, nil rated and exempted)","(b) Outward taxable supplies (zero rated)","(c ) Other outward supplies (nil rated, exempted) ","(d) Inward supplies (liable to reverse charge) ","(e) Non-GST outward supplies"]
sorted_data_table_1 =[]
sorted_data_table_1_raw =[]
k=0

 
for i in range(5):
    a=[]
    a.append(field_table_1[i])
    for j in range(5):
        a.append(table_1_data[k])
        k+=1
    #print(a)
    sorted_data_table_1_raw.append(a)
sum=[]
a=0
print('\n')
#print(sorted_data_table_1_raw)
print('\n')
dict1 = {}
for i in range(6):
    #b.append(sorted_data_table_1_raw[])
    b=[]
    for j in range(5):
        #sorted_data_table_1.append()
        b.append(sorted_data_table_1_raw[j][i])
    sorted_data_table_1.append(b)
print('\n')   
#print(sorted_data_table_1)
print('\n')   
for i in range(1,6):
    a=0
    for j in range(5):
        if sorted_data_table_1[i][j] == '-':
            a+=0
        else :
            a+=float(sorted_data_table_1[i][j])
    sorted_data_table_1[i].append(a)

sorted_data_table_1[0].append('TOTAL')
#for i in range(len(sorted_data_table_1)):
    #for j in range(len(sorted_data_table_1[i])):
        #print(sorted_data_table_1[i][j])
    #print('\n')
#print(sorted_data_table_1)
for i in range(6) :
    dict1[table_1_heading[i]] = sorted_data_table_1[i]
 
df1 = pd.DataFrame(dict1)
acvs = df1['Cess']
#print(acvs)

table_2_data = []
for i in table_2:
    if i.isdigit() or i.replace('.', '', 1).isdigit()  or i == '-':
        table_2_data.append(i)
#table_2_data = table_2[7:11]+table_2[12:16]+table_2[17:21]+table_2[23:27]+table_2[28:32]+table_2[34:38]+table_2[39:43]+table_2[44:48]+table_2[49:53]+table_2[55:59]+table_2[60:64]
table_2_heading = ["Details","Integrated tax","Central tax","State/UT tax","Cess"]
field_1_table_2 = ["(1) Import of goods","(2) Import of services","(3) Inward supplies liable to reverse charge (other than 1 & 2 above)","(4) Inward supplies from ISD","(5) All other ITC"]
field_2_table_2 = ["(1) As per rules 38,42 & 43 of CGST Rules and section 17(5)","(2) Others"]
field_3_table_2 = ["(1) ITC reclaimed which was reversed under Table 4(B)(2) in earlier tax period","(2) Ineligible ITC under section 16(4) & ITC restricted due to PoS rules"]
field_header_table_2 = ["A. ITC Available (whether in full or part)","B. ITC Reversed","C. Net ITC available (A-B)","(D) Other Details"]


sorted_data_table_2 =[]
sorted_data_table_2_raw =[]
#print(len(table_2_data))
k=0
for i in range(5):
    a=[]
    a.append(field_1_table_2[i])
    for j in range(4):
        a.append(table_2_data[k])
        k+=1
    #print(a)
    sorted_data_table_2_raw.append(a)
#print(sorted_data_table_2_raw)
#print(sorted_data_table_1_raw)
    

for i in range(5):
    b=[]
    for j in range(5):
        b.append(sorted_data_table_2_raw[j][i])
    sorted_data_table_2.append(b)
#print(sorted_data_table_2)

# total of (A)
for i in range(1,5):
    a=0
    for j in range(5):
        if sorted_data_table_2[i][j] == '-':
            a+=0
        else :
            a+=float(sorted_data_table_2[i][j])
    sorted_data_table_2[i].append(a)

sorted_data_table_2[0].append('TOTAL')
#print(sorted_data_table_2)

# data of (A)
sorted_data_table_2[0].insert(0,field_header_table_2[0])
for i in range(1,len(sorted_data_table_2)):
    sorted_data_table_2[i].insert(0,' ')
# data of (B)
sorted_data_table_2[0].append(field_header_table_2[1])
for i in range(1,len(sorted_data_table_2)):
    sorted_data_table_2[i].append(' ')

#inner data of (B)
sorted_data_table_2[0].append(field_2_table_2[0])
sorted_data_table_2[0].append(field_2_table_2[1])

sorted_data_table_2[1].append(table_2_data[20])
sorted_data_table_2[1].append(table_2_data[24])

sorted_data_table_2[2].append(table_2_data[21])
sorted_data_table_2[2].append(table_2_data[25])

sorted_data_table_2[3].append(table_2_data[22])
sorted_data_table_2[3].append(table_2_data[26])

sorted_data_table_2[4].append(table_2_data[23])
sorted_data_table_2[4].append(table_2_data[27])
#print(sorted_data_table_2)
for i in range(1,5):
    a=0
    for j in range(8,10):
        if sorted_data_table_2[i][j] == '-':
            a+=0
        else :
            a+=float(sorted_data_table_2[i][j])
    sorted_data_table_2[i].append(a)
sorted_data_table_2[0].append('TOTAL')

# data of  (C) and (D)
sorted_data_table_2[0].append(field_header_table_2[2])
sorted_data_table_2[0].append(field_header_table_2[3])

sorted_data_table_2[1].append(table_2_data[28])
sorted_data_table_2[1].append(table_2_data[32])

sorted_data_table_2[2].append(table_2_data[29])
sorted_data_table_2[2].append(table_2_data[33])

sorted_data_table_2[3].append(table_2_data[30])
sorted_data_table_2[3].append(table_2_data[34])

sorted_data_table_2[4].append(table_2_data[31])
sorted_data_table_2[4].append(table_2_data[35])

#inner data of (D)
sorted_data_table_2[0].append(field_3_table_2[0])
sorted_data_table_2[0].append(field_3_table_2[1])

sorted_data_table_2[1].append(table_2_data[36])
sorted_data_table_2[1].append(table_2_data[40])

sorted_data_table_2[2].append(table_2_data[37])
sorted_data_table_2[2].append(table_2_data[41])

sorted_data_table_2[3].append(table_2_data[38])
sorted_data_table_2[3].append(table_2_data[42])

sorted_data_table_2[4].append(table_2_data[39])
sorted_data_table_2[4].append(table_2_data[43])


dict2 = {}
for i in range(5) :
    dict2[table_2_heading[i]] = sorted_data_table_2[i]
 
df2 = pd.DataFrame(dict2)
#print(df2)

table_3_data = []
print(table_3)
for i in table_3:
    if i.isdigit() or i.replace('.', '', 1).isdigit()  or i == '-':
        table_3_data.append(i)
#print(table_3_data)
#table_3_data = table_3[7:11]+table_3[12:16]+table_3[17:21]
table_3_heading = ["Details","Integrated tax","Central tax","State/UT tax","Cess"]
field_table_3 = ["System computed Interest","Interest Paid","Late fee"]


sorted_data_table_3 =[]
sorted_data_table_3_raw =[]
#print(table_3)
k=0

 
for i in range(3):
    a=[]
    a.append(field_table_3[i])
    for j in range(4):
        a.append(table_3_data[k])
        k+=1
    #print(a)
    sorted_data_table_3_raw.append(a)
sum=[]
a=0

#print(sorted_data_table_1_raw)
dict3 = {}
for i in range(5):
    #b.append(sorted_data_table_1_raw[])
    b=[]
    for j in range(3):
        #sorted_data_table_1.append()
        b.append(sorted_data_table_3_raw[j][i])
    sorted_data_table_3.append(b)
    
#print(sorted_data_table_3)
    
for i in range(1,5):
    a=0
    for j in range(1,3):
        if sorted_data_table_3[i][j] == '-':
            a+=0
        else :
            a+=float(sorted_data_table_3[i][j])
    sorted_data_table_3[i].append(a)
sorted_data_table_3[0].append('TOTAL')


for i in range(5) :
    dict3[table_3_heading[i]] = sorted_data_table_3[i]
 
df3 = pd.DataFrame(dict3)
#print(df3)

table_4_data = table_4[20:28]+table_4[29:37]+table_4[38:46]+table_4[47:55]+table_4[58:66]+table_4[67:75]+table_4[76:84]+table_4[85:93]
table_4_heading = [table_4_heading_raw[0],table_4_heading_raw[1]+table_4_heading_raw[2],table_4_heading_raw[3],table_4_heading_raw[3]+' 2',table_4_heading_raw[3]+' 3',table_4_heading_raw[3]+' 4',table_4_heading_raw[4]+table_4_heading_raw[5],table_4_heading_raw[6]+table_4_heading_raw[7],table_4_heading_raw[8]+table_4_heading_raw[9]]
table_4_subheading = [table_4_heading_raw[10]+table_4_heading_raw[11],table_4_heading_raw[12]+table_4_heading_raw[13],table_4_heading_raw[14]+table_4_heading_raw[15],table_4_heading_raw[16]]
field_1_table_4 = [table_4[18]+table_4[19],table_4[28],table_4[37],table_4[46]]
field_2_table_4 = field_1_table_4
field_header_table_4 = [table_4[17],table_4[55]]

#print(table_4)
#print(table_4_heading)
#print(field_2_table_4)


sorted_data_table_4 =[]
sorted_data_table_4_raw =[]
#print(table_2_data)
k=0
for i in range(4):
    a=[]
    a.append(field_1_table_4[i])
    for j in range(8):
        a.append(table_4_data[k])
        k+=1
    #print(a)
    sorted_data_table_4_raw.append(a)
#print(sorted_data_table_4_raw)

for i in range(9):
    b=[]
    for j in range(4):
        b.append(sorted_data_table_4_raw[j][i])
    sorted_data_table_4.append(b)
#print(sorted_data_table_4)

for i in range(1,9):
    a=0
    for j in range(4):
        if sorted_data_table_4[i][j] == '-':
            a+=0
        else :
            a+=float(sorted_data_table_4[i][j])
    sorted_data_table_4[i].append(a)

sorted_data_table_4[0].append('TOTAL')
#print(sorted_data_table_4)

# data of (A)
sorted_data_table_4[0].insert(0,field_header_table_4[0])
for i in range(1,len(sorted_data_table_4)):
    sorted_data_table_4[i].insert(0,' ')
# data of (B)
sorted_data_table_4[0].append(field_header_table_4[1])
for i in range(1,len(sorted_data_table_4)):
    sorted_data_table_4[i].append(' ')

# inner data of (B)
for i in range(4):
    sorted_data_table_4[0].append(field_1_table_4[i])
for j in range(1,9):
    for i in range(4):
        sorted_data_table_4[j].append(table_4_data[k])
        k+=1


for i in range(1,9):
    a=0
    for j in range(7,11):
        if sorted_data_table_4[i][j] == '-':
            a+=0
        else :
            a+=float(sorted_data_table_4[i][j])
    sorted_data_table_4[i].append(a)

sorted_data_table_4[0].append('TOTAL')


sorted_data_table_4[0].insert(0,' ')
sorted_data_table_4[1].insert(0,' ')
sorted_data_table_4[2].insert(0,table_4_subheading[0])
sorted_data_table_4[3].insert(0,table_4_subheading[1])
sorted_data_table_4[4].insert(0,table_4_subheading[2])
sorted_data_table_4[5].insert(0,table_4_subheading[3])
sorted_data_table_4[6].insert(0,' ')
sorted_data_table_4[7].insert(0,' ')
sorted_data_table_4[8].insert(0,' ')

#print(sorted_data_table_4)
#print(table_4_heading)
dict4 = {}
for i in range(9) :
    dict4[table_4_heading[i]] = sorted_data_table_4[i]
 

df4 = pd.DataFrame(dict4)
print(df3)

#dict5 = {}
#for i,j in [(0,1),(2,3),(4,5),(6,7),(8,9)]:
    #dict5[details_table[i]] = [details_table[j]]
#df = pd.DataFrame(dict5)
#print(df1)
#print(df2)
#print(df3)
#print(df4)