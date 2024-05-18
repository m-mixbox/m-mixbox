import os
import os.path
import fitz
import pandas as pd 
import datetime
from datetime import date as dt
import pytz

def pdf_converter(path,specified_location):
        file_path_of_pdf = path
        doc = fitz.open(file_path_of_pdf)
        words = ''
        for i in doc :
            words+=i.get_text()
        #print(words)
        #page1 = doc[0]
        #page2 = doc[1]
        #page3 = doc[2]
        #words = page1.get_text()+page2.get_text()+page3.get_text()
        data = [] 



        data = words.split('\n')
        #print(data)
        details_table = []
        header = []
        table_1 = []
        table_2 = []
        table_3 = []
        table_4 = []
        date = []
        abc = '2(c). ARN'

        j= data.index(abc)-12
        month = data[5]

        sub = "3.1.1 Details of Supplies notified under section 9(5) of the CGST Act, 2017 and corresponding provisions in IGST/UTGST/SGST Acts"
        check = []
        check = ["3.1 Details of Outward supplies and inward supplies liable to reverse charge","3.2 Out of supplies made in 3.1 (a) above, details of inter-state supplies made","4.  Eligible ITC","5  Values of exempt, nil-rated and non-GST inward supplies","5.1 Interest and Late fee for previous tax period","6.1 Payment of tax","Breakup of tax liability declared (for interest computation)"]
        header = ["3.1 Details of Outward supplies and inward supplies liable to reverse charge","4. Eligible ITC","5.1 Interest and Late fee for previous tax period","6.1 Payment of tax"]

# getting elements in between
        if sub in data :
            if check[0] in data :
                idx1 = data.index(check[0])
                idx2 = data.index(check[1])
            else:
                idx1 = data.index('3.1 Details of Outward supplies and inward supplies liable to reverse charge (other than those covered by Table 3.1.1)')
                idx2 = data.index('3.2 Out of supplies made in 3.1 (a) and 3.1.1 (i), details of inter-state supplies made')
        else :
            if check[0] in data :
                idx1 = data.index(check[0])
                idx2 = data.index(check[1])
            else:
                idx1 = data.index('3.1 Details of Outward supplies and inward supplies liable to reverse charge (other than those covered by Table 3.1.1)')
                idx2 = data.index('3.2 Out of supplies made in 3.1 (a) and 3.1.1 (i), details of inter-state supplies made')

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



        for i in range(6,20) :
            if(i>=6 and i<=15):
               details_table.append(data[i])
        gstin = details_table[1]


        table_1_data = []
        for i in table_1:
            if i.isdigit() or i.replace('.', '', 1).isdigit()  or i == '-':
                table_1_data.append(i)
        #print(table_1)
        #print(table_1_data)
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
            sorted_data_table_1_raw.append(a)
        sum=[]
        a=0

        dict1 = {}
        for i in range(6):
            b=[]
            for j in range(5):
                b.append(sorted_data_table_1_raw[j][i])
            sorted_data_table_1.append(b)
    
        for i in range(1,6):
            a=0
            for j in range(5):
                if sorted_data_table_1[i][j] == '-':
                    a+=0
                else :
                    a+=float(sorted_data_table_1[i][j])
            sorted_data_table_1[i].append(a)

        sorted_data_table_1[0].append('TOTAL')
        for i in range(6) :
            dict1[table_1_heading[i]] = sorted_data_table_1[i]
 
        df1 = pd.DataFrame(dict1)

        table_2_data = []
        for i in table_2:
            if i.isdigit() or i.replace('.', '', 1).isdigit()  or i == '-':
                table_2_data.append(i)

        table_2_heading = ["Details","Integrated tax","Central tax","State/UT tax","Cess"]
        field_1_table_2 = ["(1) Import of goods","(2) Import of services","(3) Inward supplies liable to reverse charge (other than 1 & 2 above)","(4) Inward supplies from ISD","(5) All other ITC"]
        field_2_table_2 = ["(1) As per rules 38,42 & 43 of CGST Rules and section 17(5)","(2) Others"]
        field_3_table_2 = ["(1) ITC reclaimed which was reversed under Table 4(B)(2) in earlier tax period","(2) Ineligible ITC under section 16(4) & ITC restricted due to PoS rules"]
        field_header_table_2 = ["A. ITC Available (whether in full or part)","B. ITC Reversed","C. Net ITC available (A-B)","(D) Other Details"]


        sorted_data_table_2 =[]
        sorted_data_table_2_raw =[]

        k=0
        for i in range(5):
            a=[]
            a.append(field_1_table_2[i])
            for j in range(4):
                a.append(table_2_data[k])
                k+=1
            sorted_data_table_2_raw.append(a)

        for i in range(5):
            b=[]
            for j in range(5):
                b.append(sorted_data_table_2_raw[j][i])
            sorted_data_table_2.append(b)

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

        table_3_data = []
        for i in table_3:
            if i.isdigit() or i.replace('.', '', 1).isdigit()  or i == '-':
                table_3_data.append(i)

        table_3_heading = ["Details","Integrated tax","Central tax","State/UT tax","Cess"]
        field_table_3 = ["System computed Interest","Interest Paid","Late fee"]


        sorted_data_table_3 =[]
        sorted_data_table_3_raw =[]

        k=0

 
        for i in range(3):
            a=[]
            a.append(field_table_3[i])
            for j in range(4):
                a.append(table_3_data[k])
                k+=1
    
            sorted_data_table_3_raw.append(a)
        sum=[]
        a=0


        dict3 = {}
        for i in range(5):
            b=[]
            for j in range(3):
                b.append(sorted_data_table_3_raw[j][i])
            sorted_data_table_3.append(b)
    

    
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

        table_4_data = table_4[20:28]+table_4[29:37]+table_4[38:46]+table_4[47:55]+table_4[58:66]+table_4[67:75]+table_4[76:84]+table_4[85:93]
        table_4_heading = ["Description","Total tax payable","Tax paid through ITC","Tax paid through ITC 2","Tax paid through ITC 3","Tax paid through ITC 4","Tax paid in cash","Interest paid in cash","Late fee paid in cash"]
        table_4_subheading = ["Integrated tax","Central tax","State/UT tax","Cess"]
        field_1_table_4 = [table_4[18]+table_4[19],table_4[28],table_4[37],table_4[46]]
        field_2_table_4 = field_1_table_4
        field_header_table_4 = [table_4[17],table_4[55]]


        sorted_data_table_4 =[]
        sorted_data_table_4_raw =[]

        k=0
        for i in range(4):
            a=[]
            a.append(field_1_table_4[i])
            for j in range(8):
                a.append(table_4_data[k])
                k+=1
            sorted_data_table_4_raw.append(a)


        for i in range(9):
            b=[]
            for j in range(4):
                b.append(sorted_data_table_4_raw[j][i])
            sorted_data_table_4.append(b)

        for i in range(1,9):
            a=0
            for j in range(4):
                if sorted_data_table_4[i][j] == '-':
                    a+=0
                else :
                    a+=float(sorted_data_table_4[i][j])
            sorted_data_table_4[i].append(a)
        sorted_data_table_4[0].append('TOTAL')

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


        dict4 = {}
        for i in range(9) :
            dict4[table_4_heading[i]] = sorted_data_table_4[i]
 

        df4 = pd.DataFrame(dict4)

        dict5 = {}
        for i,j in [(0,1),(2,3),(4,5),(6,7),(8,9)]:
            dict5[details_table[i]] = [details_table[j]]
        df = pd.DataFrame(dict5)
    
        #N = 5

        #res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=N))
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        folder = str(dt.today())+ '___'+ str(current_time.hour) + '_' + str(current_time.minute) +'_' + str(current_time.second)
        folder.replace('-','_')
        excel_file_name = specified_location+'/'+gstin+'_'+month+'_'+folder+'.xlsx'
        with open(excel_file_name, 'w') as fp:
            pass
        with pd.ExcelWriter(excel_file_name) as writer:
            df.to_excel(writer, sheet_name="table1", index=False)
            df1.to_excel(writer, sheet_name="table1", index=False,startrow=8)
            df2.to_excel(writer, sheet_name="table2", index=False)
            df3.to_excel(writer, sheet_name="table3", index=False)
            df4.to_excel(writer, sheet_name="table4", index=False)
        #excel_file_url = 'The URL To The Excel Sheet : '+os.path.abspath(excel_file_name)
        #return excel_file_url,'file:///'+os.path.abspath(excel_file_name),[df1,df2,df3,df4]
        return gstin+'_'+month+'_'+folder+'.xlsx'
    
def create_directory():
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        time = str(current_time.hour) + '-' + str(current_time.minute) +'-' + str(current_time.second)
        directory = str(date.today())+ ' ' +time
        parent_dir = "D:/excel/"
        path = os.path.join(parent_dir, directory) 
        error = ''
        try:
            os.makedirs(path, exist_ok = True)
            print("Directory '%s' created successfully" % directory) 
            error = ''
        except OSError as error:
            print(error)
        return error,path
    
def scan_directory(path):
        filenames = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if(file.endswith(".pdf")):
                    filenames.append(os.path.join(root,file))
        return filenames
    
def pdf_files_validator(file_path):
        year_list = []
        month_list = []
        gstin_list = []
        month = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
        for i in file_path:
            pdf_name = os.path.basename(i).split('/')[-1]
            _,gstin,fp = pdf_name.split('_')
            a,b = fp.split('.')
            year,month = a[2:],a[:2]
            if month == '01' or month == '02' or month == '03':
                year_list.append(int(year)-1)
                month_list.append(int(month)+12)
                gstin_list.append(gstin)
            else :
                year_list.append(int(year))
                month_list.append(int(month))
                gstin_list.append(gstin)
        check_gstin = all(ele == gstin_list[0] for ele in gstin_list)
        check_year = all(ele == year_list[0] for ele in year_list)
        def is_arithmetic(l):
            delta = l[1] - l[0]
            for index in range(len(l) - 1):
                if not (l[index + 1] - l[index] == delta):
                    return False
            return True
        if(check_gstin):
            if(check_year):
                if(len(month_list) == len(set(month_list))) :
                    if is_arithmetic(sorted(month_list)):
                        result='The Pdf File Has Been Converted To CSV'
                    else :
                        result='The Pdf File has some months data missing'
                else :
                    pos = [x for x in month_list if month_list.count(x) < 1]
                    if len(pos) > 1 :
                        result='There are missing files of '
                        for i in pos :
                            result += ' ' + i
                        pass
                    else :
                        result='There is a missing file of '+month[pos[0]]
            else:
                result='Pdf files are not of same year'
        else:
            result='Pdf files have different gstin'
        return result

def consolidated_sheet_generator(df_list,specified_location):
        excel_file_name = specified_location+'/consolidated_sheet'+'.xlsx'
        header = [["Nature of Supplies","Total taxable value","Integrated tax","Central tax","State/UT tax","Cess"],["Details","Integrated tax","Central tax","State/UT tax","Cess"],["Details","Integrated tax","Central tax","State/UT tax","Cess"],['Description', 'Total tax payable', 'Tax paid through ITC', 'Tax paid through ITC 2', 'Tax paid through ITC 3', 'Tax paid through ITC 4', 'Tax paid in cash', 'Interest paid in cash', 'Late fee paid in cash']]
        name = 'table'
        k=0
        xyz= []
        a = 0
        b = []
        c = []
        with open(excel_file_name, 'w') as fp:
            pass
        with pd.ExcelWriter(excel_file_name) as writer:
            for j in range(len(df_list)) :
                #name = 'table'
                for  i in range(len(df_list[j])):
                    #name +=str(k)
                    xyz.append(df_list[j][i].values.tolist())
            
            c = []
            for k in range(1,6):
                b= []
                for j in range (6):
                    a=0
                    for i in range(0,len(xyz),4):
                        #print(xyz[i][j][k])
                        if type(xyz[i][j][k]) == type(12.00):
                            a+=xyz[i][j][k]
                        elif xyz[i][j][k] == '-':
                            a+=0
                        else :
                            a+=float(xyz[i][j][k])
                    b.append(a)
                c.append(b)
            for k in range(1,5):
                b= []
                d=''
                for j in range (15):
                    a=0
                    for i in range(1,len(xyz)+1,4):
                        #print(xyz[i][j][k])
                        if type(xyz[i][j][k]) == type(12.00):
                            a+=xyz[i][j][k]
                        elif xyz[i][j][k] == '-':
                            a+=0
                        elif xyz[i][j][k] == ' ' :
                            pass
                        else :
                            a+=float(xyz[i][j][k])
                    b.append(a)
                c.append(b)
            for k in range(1,5):
                b= []
                for j in range (4):
                    a=0
                    for i in range(2,len(xyz)+2,4):
                        #print(xyz[i][j][k])
                        if type(xyz[i][j][k]) == type(12.00):
                            a+=xyz[i][j][k]
                        elif xyz[i][j][k] == '-':
                            a+=0
                        else :
                            a+=float(xyz[i][j][k])
                    b.append(a)
                c.append(b)
            for k in range(1,9):
                b= []
                for j in range (1,13):
                    a=0
                    d=''
                    for i in range(3,len(xyz)+3,4):
                        #print(xyz[i][j][k])
                        if type(xyz[i][j][k]) == type(12.00):
                            a+=xyz[i][j][k]
                        elif xyz[i][j][k] == '-':
                            a+=0
                        elif xyz[i][j][k] == ' ' :
                            pass
                        else :
                            a+=float(xyz[i][j][k])
                    b.append(a)
                c.append(b)
            table_1_data = c[:5]
            table_2_data = c[5:9]
            table_3_data = c[9:13]
            table_4_data = c[13:]

            sorted_data_table_1 =[["(a) Outward taxable supplies (other than zero rated, nil rated and exempted)","(b) Outward taxable supplies (zero rated)","(c ) Other outward supplies (nil rated, exempted) ","(d) Inward supplies (liable to reverse charge) ","(e) Non-GST outward supplies","Total"],table_1_data[0],table_1_data[1],table_1_data[2],table_1_data[3],table_1_data[4]]
            dict1 = {}
            for i in range(6) :
                dict1[header[0][i]] = sorted_data_table_1[i]
 
            df1 = pd.DataFrame(dict1)

            sorted_data_table_2 =[["A. ITC Available (whether in full or part)","(1) Import of goods","(2) Import of services","(3) Inward supplies liable to reverse charge (other than 1 & 2 above)","(4) Inward supplies from ISD","(5) All other ITC","Total","B. ITC Reversed","(1) As per rules 38,42 & 43 of CGST Rules and section 17(5)","(2) Others","Total","C. Net ITC available (A-B)","(D) Other Details","(1) ITC reclaimed which was reversed under Table 4(B)(2) in earlier tax period","(2) Ineligible ITC under section 16(4) & ITC restricted due to PoS rules"],table_2_data[0],table_2_data[1],table_2_data[2],table_2_data[3]]
        
            dict2 = {}
        
            for i in range(5) :
                dict2[header[1][i]] = sorted_data_table_2[i]
 
            df2 = pd.DataFrame(dict2)
      
            sorted_data_table_3 =[["System computed Interest","Interest Paid","Late fee","Total"],table_3_data[0],table_3_data[1],table_3_data[2],table_3_data[3]]
        
            dict3 = {}
        
            for i in range(5) :
                dict3[header[2][i]] = sorted_data_table_3[i]
 
            df3 = pd.DataFrame(dict3)


            sorted_data_table_4 =[["(A) Other than reverse charge","Integrated tax","Central tax","State/UT tax","Cess","Total","(B) Reverse charge","Integrated tax","Central tax","State/UT tax","Cess","Total"],table_4_data[0],table_4_data[1],table_4_data[2],table_4_data[3],table_4_data[4],table_4_data[5],table_4_data[6],table_4_data[7]]
        
            dict4 = {}
        
            for i in range(9) :
                dict4[header[3][i]] = sorted_data_table_4[i]
 
            df4 = pd.DataFrame(dict4)
            df1.to_excel(writer, sheet_name="table1", index=False,startrow=8)
            df2.to_excel(writer, sheet_name="table2", index=False)
            df3.to_excel(writer, sheet_name="table3", index=False)
            df4.to_excel(writer, sheet_name="table4", index=False)


        pass

