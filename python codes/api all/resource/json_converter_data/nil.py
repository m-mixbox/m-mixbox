
import pandas as pd
import json

def nil_generater(path_of_json_file ):

   with open(path_of_json_file) as f:
      raw_data = json.load(f)

   gstin = raw_data['gstin']
   nil_data = []

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

   df = pd.DataFrame(dict)
   return df
#print(df)