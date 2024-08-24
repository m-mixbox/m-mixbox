

import pandas as pd

import json


path_of_json_file = r"D:\New folder\cgl gs\static gk\returns_16082024_R1_20AAUCA7296F1ZE_offline_others_0 (10)\returns_16082024_R1_20AAUCA7296F1ZE_offline_others_0.json"

with open(path_of_json_file) as f:
   raw_data = json.load(f)
gstin = raw_data['gstin']
def b2b_line_item(raw_data):


    gstin = raw_data['gstin']

    b2b_data = raw_data['b2b'][0]
    invoice_data = b2b_data['inv']
    ctin = b2b_data['ctin']
    fp = raw_data['fp']
    fp1 = fp[:2]
    fp2 = fp[2:]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July',
          'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    fp1 = months[int(fp1)-1]
    fp = fp1+'-'+fp2
    filling_period = []
    invoice_number = []
    invoice_type = []
    reverse_charge = []
    total_invoice = []
    #these variables takes data from items
    igst = []
    cgst = []
    sgst = []
    tax_amount = []
    invoice_date = []
    c_gstin = [ ]
    t_gstin = []

    for a in range(len(raw_data['b2b'])) :
        b2b_data = raw_data['b2b'][a]
        invoice_data = b2b_data['inv']
        ctin = b2b_data['ctin']
        for i in invoice_data:
            for j in range(len(i['itms'])) :
                invoice_date.append(i['idt'])
                invoice_number.append(i['inum'])
                invoice_type.append(i['inv_typ'])
                reverse_charge.append(i['rchrg'])
                total_invoice.append(i['val'])
                more_invoice_data = i['itms'][j]['itm_det']
                if 'iamt' not in more_invoice_data  :
                    igst.append(0)
                else :
                    igst.append(more_invoice_data['iamt'])
                if 'camt' not in more_invoice_data :
                    cgst.append(0)
                else :
                    cgst.append(more_invoice_data['camt'])
                if 'samt' not in more_invoice_data :
                    sgst.append(0)
                else :
                    sgst.append(more_invoice_data['samt'])
                tax_amount.append(more_invoice_data['txval'])
                filling_period.append(fp)
                t_gstin.append(gstin)
                c_gstin.append(ctin)

    data =[t_gstin,filling_period ,c_gstin,c_gstin,invoice_number,invoice_date,invoice_type,reverse_charge,tax_amount,igst,cgst,sgst,total_invoice]

    dict = {}
    header = ['TAXPAYER GSTIN','FILLING PERIOD', 'CUSTOMER GSTIN ','CUSTOMER NAME','INVOICE NUMBER ','INVOICE DATE','INVOICE TYPE','REVERSE CHARGE','TAXABLE AMOUNT','IGST AMOUNT','CGST AMOUNT','SGST AMOUNT','TOTAL']
    for i in range(len(header)) :
        dict[header[i]] = data[i]

    return pd.DataFrame(dict)
def b2b(raw_data):
    gstin = raw_data['gstin']

    b2b_data = raw_data['b2b'][0]
    invoice_data = b2b_data['inv']
    ctin = b2b_data['ctin']
    fp = raw_data['fp']
    fp1 = fp[:2]
    fp2 = fp[2:]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July',
          'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    fp1 = months[int(fp1)-1]
    fp = fp1+'-'+fp2
    filling_period = []
    invoice_number = []
    invoice_type = []
    reverse_charge = []
    total_invoice = []
#these variables takes data from items
    igst = []
    cgst = []
    sgst = []
    tax_amount = []
    invoice_date = []
    c_gstin = [ ]
    t_gstin = []

    for a in range(len(raw_data['b2b'])) :
        b2b_data = raw_data['b2b'][a]
        invoice_data = b2b_data['inv']
        ctin = b2b_data['ctin']
        for i in invoice_data:
            invoice_date.append(i['idt'])
            invoice_number.append(i['inum'])
            invoice_type.append(i['inv_typ'])
            reverse_charge.append(i['rchrg'])
            total_invoice.append(i['val'])
            cg=sg=tx=ig=0
            for j in range(len(i['itms'])) :
                more_invoice_data = i['itms'][j]['itm_det']
                if 'iamt' not in more_invoice_data  :
                    ig+=0
                else :
                    ig+=more_invoice_data['iamt']
                if 'camt' not in more_invoice_data :
                    cg+=0
                else :
                    cg+=more_invoice_data['camt']
                if 'samt' not in more_invoice_data :
                    sg+=0
                else :
                    sg+=more_invoice_data['samt']
         #cg+=more_invoice_data['camt']
         #sg+=more_invoice_data['samt']
                tx+=more_invoice_data['txval']
            cgst.append(cg)
            igst.append(ig)
            sgst.append(sg)
            tax_amount.append(tx)
            filling_period.append(fp)
            t_gstin.append(gstin)
            c_gstin.append(ctin)
#print(cgst)
    data =[t_gstin,filling_period ,c_gstin,c_gstin,invoice_number,invoice_date,invoice_type,reverse_charge,tax_amount,igst,cgst,sgst,total_invoice]

    dict = {}
    header = ['TAXPAYER GSTIN','FILLING PERIOD', 'CUSTOMER GSTIN ','CUSTOMER NAME','INVOICE NUMBER ','INVOICE DATE','INVOICE TYPE','REVERSE CHARGE','TAXABLE AMOUNT','IGST AMOUNT','CGST AMOUNT','SGST AMOUNT','TOTAL']
    for i in range(len(header)) :
        dict[header[i]] = data[i]

    return pd.DataFrame(dict)
def nil(raw_data):
    
    gstin = raw_data['gstin']
    nil_data = []
    if 'nil'  in raw_data:
        nil_data = raw_data['nil']['inv']
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
    non_gst_amount = []
    exempt_amount = []
#these variables takes data from items
    nil_amount = []


    for i in nil_data:
        supply_type.append(i['sply_ty'])
        exempt_amount.append(i['expt_amt'])
        nil_amount.append(i['nil_amt'])
        non_gst_amount.append(i['ngsup_amt'])
    t_gstin = []
    for x in range(len(nil_data)):
        t_gstin.append(gstin)
        filling_period.append(fp)
    data =[t_gstin,filling_period ,exempt_amount,nil_amount,non_gst_amount,supply_type]

    dict = {}
    header = ['TAXPAYER GSTIN','FILLING PERIOD', 'EXEMPT AMOUNT ','NIL AMOUNT','NON-GST SUPPLY AMOUNT ','SUPPLY TYPE']
    for i in range(len(header)) :
        dict[header[i]] = data[i]

    return pd.DataFrame(dict)
def b2cs(raw_data):
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

    return pd.DataFrame(dict)

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()


path_of_excel_file = r"D:\{gstin}.xlsx".format(gstin=gstin)

f = open(path_of_excel_file,"w+")
with pd.ExcelWriter(path_of_excel_file) as writer:
   
    # use to_excel function and specify the sheet_name and index 
    # to store the dataframe in specified sheet
    
    if 'b2b' in raw_data :
      df1 = b2b(raw_data=raw_data)
      df2 = b2b_line_item(raw_data)
      df1.to_excel(writer, sheet_name="b2b", index=False)
      df2.to_excel(writer, sheet_name="b2b line items", index=False)
    if 'b2cs' in raw_data :
      df3 = b2cs(raw_data)
      df3.to_excel(writer, sheet_name="b2cs", index=False)
    if 'nil' in raw_data :
      df4 = nil(raw_data)
      df4.to_excel(writer, sheet_name="nil", index=False)