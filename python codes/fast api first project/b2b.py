import pandas as pd
import json

def b2b_generter(path_of_json_file):

   with open(path_of_json_file) as f:
      raw_data = json.load(f)

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

   df = pd.DataFrame(dict)

   return df