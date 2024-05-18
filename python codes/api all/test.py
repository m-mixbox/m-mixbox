from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os

app = FastAPI()

FILE_FOLDER = "files"

@app.post("/download/")
async def download_file():
    try:
        #file_name = r'converted\pdf_to_excel'
        file_path = os.path.join(os.path.dirname(__file__), "uploads\\pdf\\GSTR3B_10AAHCB3756A1ZC_012023.pdf")
        file_name = 'GSTR3B_10AAHCB3756A1ZC_012023.pdf'
        #if not os.path.exists(file_path):
        #    raise HTTPException(status_code=404, detail="File not found")

        # Explicitly specify the MIME type for .docx files
        return FileResponse(file_path,media_type="application/pdf",filename=file_name, headers={"Content-Disposition": f"attachment; filename={file_name}"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to download file: {str(e)}")
