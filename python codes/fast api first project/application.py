
from fileinput import filename
from flask import Flask, render_template,url_for,request,send_file
import os
import os.path
from pathlib import WindowsPath
import pandas as pd
import json 

# LOCAL DIRECTORY IMPORTS
import excel_to_pdf as ex
import ocr_image_ as ocr_image
import b2b
import b2b_line_items
import b2cs
import nil
import xml_tree_generator as x_tree

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/download')
def download_file():
	#path = "html2pdf.pdf"
	#path = "info.xlsx"
	path = "simple.docx"
	#path = "sample.txt"
	return send_file(path, as_attachment=True)

@app.route('/ocr/')
def ocr():
    return render_template('ocr.html')

@app.route('/pdf/')
def pdf():
    return render_template('pdf to excel.html')

@app.route('/json_/')
def json_():
    return render_template('json to excel.html')

@app.route('/excel/')
def excel():
    return render_template('excel to tally.html')

@app.route('/convert_excel/',methods = ["POST"])                    
def convert_excel(): 
    
    def excel_converter(path):
            if os.path.isfile(path):
                result = 'The Pdf File Has Been Converted To CSV'
                directory = x_tree.xml_generater(path)
                
                file_url,link = directory,''
            else :
                filenames = ex.scan_directory(path)
                result = ''
                file_url = ''
                link = ''
            return result,file_url,link
        
    
    if request.method == "POST" :
        input_data = [(x[1])  for x in request.form.items() ]
        pdf_file_path = str(input_data[0])
        path = WindowsPath(pdf_file_path.replace('"', ''))
        if os.path.exists(path):
            result,excel_file_url,link = excel_converter(path)
        else:
            result = 'This URL Does not exists'
            excel_file_url = ''
            link = ''
        return render_template("excel to tally converted.html", res=result,url = excel_file_url,link = link)
        #return 'abc'
    else :
        return "404 error"

@app.route('/convert_pdf/',methods = ["POST"])                    
def convert_pdf(): 
    
    def pdf_converter(path):
            if os.path.isfile(path):
                result = 'The Pdf File Has Been Converted To CSV'
                error,directory = ex.create_directory()
                
                excel_file_url,link,_ = ex.pdf_converter(path,directory)
            else :
                filenames = ex.scan_directory(path)
                result = ex.pdf_files_validator(filenames)
                if len(filenames) == 12 :
                    if result == 'The Pdf File Has Been Converted To CSV' :
                        error,directory = ex.create_directory()
                        dataframes_list = []
                        for i in filenames:
                            excel_file_url,link,x = ex.pdf_converter(i,directory)
                            dataframes_list.append(x)
                
                        ex.consolidated_sheet_generator(dataframes_list,directory)
                        #result='The Pdf File Has Been Converted To CSV'
                        excel_file_url = directory
                        link = directory
                    else :
                        excel_file_url = ''
                        link = ''
                elif len(filenames) < 12 :
                    warn = 'pdf files are less than 12 are you sure you want to continue'
                    if result == 'The Pdf File Has Been Converted To CSV' :
                        error,directory = ex.create_directory()
                        dataframes_list = []
                        for i in filenames:
                            excel_file_url,link,x = ex.pdf_converter(i,directory)
                            dataframes_list.append(x)
                
                        ex.consolidated_sheet_generator(dataframes_list,directory)
                        #result='The Pdf File Has Been Converted To CSV'
                        excel_file_url = directory
                        link = directory
                    else :
                        excel_file_url = ''
                        link = ''
                elif len(filenames) > 12 :
                    result = ' file count exceeded'
                    excel_file_url = ''
                    link = ''
                else :
                    excel_file_url = ''
                    link = ''
            return result,excel_file_url,link
        
    
    if request.method == "POST" :
        input_data = [(x[1])  for x in request.form.items() ]
        pdf_file_path = str(input_data[0])
        path = WindowsPath(pdf_file_path.replace('"', ''))
        if os.path.exists(path):
            result,excel_file_url,link = pdf_converter(path)
        else:
            result = 'This URL Does not exists'
            excel_file_url = ''
            link = ''
        return render_template("pdf to excel.html", res=result,url = excel_file_url,link = link)
        #return 'abc'
    else :
        return "404 error"
    
@app.route('/convert_json/',methods = ["POST"])                    
def convert_json(): 
    
    def json_converter(path):
            if os.path.isfile(path):
                result = 'The Pdf File Has Been Converted To CSV'
                path_of_json_file = path
                with open(path_of_json_file) as f:
                    raw_data = json.load(f)

                df1 = pd.DataFrame()
                df2 = pd.DataFrame()
                df3 = pd.DataFrame()
                df4 = pd.DataFrame()
                
                error,directory = ex.create_directory()
                path_of_excel_file = directory+ '/'+'data'+'.excel'
                file_url = path_of_excel_file
                link =''
                with pd.ExcelWriter(path_of_excel_file) as writer:
    
                    if 'b2b' in raw_data :
                        df1 = b2b.b2b_generter(path)
                        df2 = b2b_line_items.b2b_line_items_generater(path)
                        df1.to_excel(writer, sheet_name="b2b", index=False)
                        df2.to_excel(writer, sheet_name="b2b line items", index=False)
                    if 'b2cs' in raw_data :
                        df3 = b2cs.b2cs_generater(path)
                        df3.to_excel(writer, sheet_name="b2b line items", index=False)
                    if 'nil' in raw_data :
                        df4 = nil.nil_generater(path)
                        df4.to_excel(writer, sheet_name="b2b line items", index=False)
            else :
                filenames = ex.scan_directory(path)
                result = ''
                file_url = ''
                link = ''

            return result,file_url,link
        
    
    if request.method == "POST" :
        input_data = [(x[1])  for x in request.form.items() ]
        pdf_file_path = str(input_data[0])
        path = WindowsPath(pdf_file_path.replace('"', ''))
        if os.path.exists(path):
            result,excel_file_url,link = json_converter(path)
        else:
            result = 'This URL Does not exists'
            excel_file_url = ''
            link = ''
        return render_template("json to excel.html", res=result,url = excel_file_url,link = link)
        #return 'abc'
    else :
        return "404 error"
    
@app.route('/generate_ocr/',methods = ["POST"])                    
def generate_ocr(): 
    
    def image_converter():
            if os.path.isfile(path):
                result = 'The Image Has Been Converted To Word File'
                file_url,link = ocr_image.ocr_converter(path)
            else :
                result = ''
                file_url = ''
                link = ''
            return result,file_url,link
        
    
    if request.method == "POST" :
        input_data = [(x[1])  for x in request.form.items() ]
        pdf_file_path = str(input_data[0])
        path = WindowsPath(pdf_file_path.replace('"', ''))
        if os.path.exists(path):
            result,file_url,link = image_converter()
        else:
            result = 'This URL Does not exists'
            file_url = ''
            link = ''
        return render_template("ocr.html", res=result,url = file_url,link = link)
        #return 'abc'
    else :
        return "404 error"

if __name__ == '__main__':
   app.run(debug=True)