import os
import os.path
filenames = []
path = r'C:\Users\MBSPL-Ayush\Desktop\Bihar\Bihar'
for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".pdf")):
            filenames.append(os.path.join(root,file))
year_list = []
month_list = []
gstin_list = []
for i in filenames:
    pdf_name = os.path.basename(i).split('/')[-1]
    _,gstin,fp = pdf_name.split('_')
    a,b = fp.split('.')
    year,month = a[2:],a[:2]
    if month == '01' or month == '02' or month == '03':
                year_list.append(int(year)-1)
                month_list.append(int(month))
                gstin_list.append(gstin)
    else :
                year_list.append(int(year))
                month_list.append(int(month))
                gstin_list.append(gstin)
print(year_list)
check_gstin = all(ele == gstin_list[0] for ele in gstin_list)
check_year = all(ele == year_list[0] for ele in year_list)
check_month = all(ele != year_list[0] for ele in month_list)
print(check_gstin)
print(check_year)
if(check_gstin):
    if(check_year):
        if(check_month):
            print(list(x for x in month_list if 1 <= x <= 12))
    else:
        pass
else:
    pass
