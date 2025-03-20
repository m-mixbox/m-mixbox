import os
import random
import string
from flask import Flask, request, send_file, jsonify
from io import BytesIO
from docx import Document
from docx.shared import Inches
from pathlib import Path
import traceback
from sbi import *

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"  # Or specify a domain
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response
# Directory to store images and generated files
local_path = os.path.dirname(__file__)
image_dir = os.path.join(local_path,"images")
output_dir = os.path.join(local_path,"generated")

# Helper function to generate a random 7-character string for filenames
def generate_random_filename(length=7):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/generate-docx/', methods=['POST'])
def generate_docx():
    try:
        print("Starting DOCX generation process...")

        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        values_list = list(data.values())
                # Generate a random filename
        random_filename = generate_random_filename() + ".docx"
        output_path = os.path.join(output_dir,random_filename)
        abc = sbi_format(local_path,image_dir,output_dir,values_list,random_filename,output_path)

        # Send the saved file
        return send_file(
            output_path,
            as_attachment=True,
            download_name=random_filename,
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        traceback.print_exc()
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
