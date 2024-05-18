from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import mimetypes
from fastapi.responses import FileResponse
import datetime
import pytz
from datetime import date as dt
import json
import logging

#local imports
from resource.ocr_data.pytesseract_ocr import *
from resource.excel_converter_data.xml_tree_generator import * 
from resource.pdf_converter_data.pdf_to_excel import *
from resource.json_converter_data.b2b import *
from resource.json_converter_data.b2b_line_items import *
from resource.json_converter_data.b2cs import *
from resource.json_converter_data.nil import *

app = FastAPI()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler and set its level to DEBUG
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Create a formatter and set the formatter for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)
logger.debug('api started')

UPLOAD_FOLDER = "uploads"
DOWNLOAD_FOLDER = "converted"

def is_valid_file(filename, allowed_types):
    mimetype, _ = mimetypes.guess_type(filename)
    return mimetype in allowed_types

def save_file(file, file_path):
    with open(file_path, "wb") as buffer:
        buffer.write(file)

@app.post("/upload/image/")
async def upload_image(file: UploadFile = File(...)):
    logger.debug('/image/ endpoint accessed')
    try:
        logger.debug(f"Received file: {file.filename}")
        os.makedirs(os.path.join(UPLOAD_FOLDER, "images"), exist_ok=True)
        file_path = os.path.join(UPLOAD_FOLDER, "images", file.filename)
        save_file(await file.read(), file_path)

        if os.path.getsize(file_path) == 0:
            os.remove(file_path)
            raise HTTPException(status_code=400, detail="Uploaded file is empty")

        if not is_valid_file(file_path, ["image/jpeg", "image/png"]):
            os.remove(file_path)
            raise HTTPException(status_code=400, detail="Uploaded file is not an image")
        os.makedirs(os.path.join(DOWNLOAD_FOLDER, "image_to_docx"), exist_ok=True)
        output_path = os.path.join(DOWNLOAD_FOLDER, "image_to_docx")
        output_file = extract_text(file_path,output_path)
        return_file = os.path.join(output_path,output_file)
        #print(return_file)
        logger.debug(f"Sent file: {output_file}")
        return FileResponse(return_file,media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",filename=output_file)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to upload image: {str(e)}")

@app.post("/upload/json/")
async def upload_json(file: UploadFile = File(...)):
    logger.debug('/json/ endpoint accessed')
    try:
        logger.debug(f"Received file: {file.filename}")
        os.makedirs(os.path.join(UPLOAD_FOLDER, "json"), exist_ok=True)
        file_path = os.path.join(UPLOAD_FOLDER, "json", file.filename)
        save_file(await file.read(), file_path)

        if os.path.getsize(file_path) == 0:
            os.remove(file_path)
            raise HTTPException(status_code=400, detail="Uploaded file is empty")

        if not is_valid_file(file_path, ["application/json"]):
            os.remove(file_path)
            raise HTTPException(status_code=400, detail="Uploaded file is not a JSON file")
        os.makedirs(os.path.join(DOWNLOAD_FOLDER, "json to excel"), exist_ok=True)
        output_path = os.path.join(DOWNLOAD_FOLDER, "json to excel")

        with open(file_path) as f:
                    raw_data = json.load(f)

        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        df3 = pd.DataFrame()
        df4 = pd.DataFrame()
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        directory = str(dt.today())+ '___'+ str(current_time.hour) + '_' + str(current_time.minute) +'_' + str(current_time.second)
        directory.replace('-','_')
        path_of_excel_file = output_path+ '/'+directory+'.xlsx'
        excel_filename = directory+'.xlsx'
        with pd.ExcelWriter(path_of_excel_file,engine='xlsxwriter') as writer:
                    if 'b2b' in raw_data :
                        df1 = b2b_generter(file_path)
                        df2 = b2b_line_items_generater(file_path)
                        df1.to_excel(writer, sheet_name="b2b", index=False)
                        df2.to_excel(writer, sheet_name="b2b line items", index=False)
                    if 'b2cs' in raw_data :
                        df3 = b2cs_generater(file_path)
                        df3.to_excel(writer, sheet_name="b2b line items", index=False)
                    if 'nil' in raw_data :
                        df4 = nil_generater(file_path)
                        df4.to_excel(writer, sheet_name="b2b line items", index=False)
        logger.debug(f"Sent file: {excel_filename}")
        return FileResponse(path_of_excel_file,media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",filename=excel_filename)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to upload JSON file: {str(e)}")

@app.post("/upload/pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    logger.debug('/pdf/ endpoint accessed')
    try:
        logger.debug(f"Received file: {file.filename}")
        os.makedirs(os.path.join(UPLOAD_FOLDER, "pdf"), exist_ok=True)
        file_path = os.path.join(UPLOAD_FOLDER, "pdf", file.filename)
        save_file(await file.read(), file_path)

        if os.path.getsize(file_path) == 0:
            os.remove(file_path)
            raise HTTPException(status_code=400, detail="Uploaded file is empty")

        if not is_valid_file(file_path, ["application/pdf"]):
            os.remove(file_path)
            raise HTTPException(status_code=400, detail="Uploaded file is not a PDF file")
        os.makedirs(os.path.join(DOWNLOAD_FOLDER, "pdf_to_excel"), exist_ok=True)
        output_path = os.path.join(DOWNLOAD_FOLDER, "pdf_to_excel")
        
        output_file = pdf_converter(file_path,output_path)
        return_file = os.path.join(output_path,output_file)
        #return {'directory':return_file}
        logger.debug(f"Sent file: {output_file}")
        return FileResponse(return_file,media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",filename=output_file)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to upload PDF file: {str(e)}")

@app.post("/upload/excel/")
async def upload_excel(file: UploadFile = File(...)):
    logger.debug('/excel/ endpoint accessed')
    try:
        logger.debug(f"Received file: {file.filename}")
        os.makedirs(os.path.join(UPLOAD_FOLDER, "excel"), exist_ok=True)
        file_path = os.path.join(UPLOAD_FOLDER, "excel", file.filename)
        save_file(await file.read(), file_path)

        if os.path.getsize(file_path) == 0:
            os.remove(file_path)
            raise HTTPException(status_code=400, detail="Uploaded file is empty")

        if not is_valid_file(file_path, ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/vnd.ms-excel"]):
            os.remove(file_path)
            raise HTTPException(status_code=400, detail="Uploaded file is not an Excel file")
        os.makedirs(os.path.join(DOWNLOAD_FOLDER, "excel_to_xml"), exist_ok=True)
        output_path = os.path.join(DOWNLOAD_FOLDER, "excel_to_xml")
        output_file = xml_generater(file_path,output_path)
        return_file = os.path.join(output_path,output_file)
        logger.debug(f"Sent file: {output_file}")
        return FileResponse(return_file,media_type="application/xml",filename=output_file)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to upload Excel file: {str(e)}")
