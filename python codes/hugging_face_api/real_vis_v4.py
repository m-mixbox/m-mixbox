import requests
import string
import random
import os

API_URL = "https://api-inference.huggingface.co/models/SG161222/RealVisXL_V4.0"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

# You can access the image with PIL.Image for example
image_byte = query({"inputs": "happy mothers day poster, circular design, 3d effect, digital style, floral, digital drawing"})
import io
from PIL import Image
for i in range(1):
	
    image = Image.open(io.BytesIO(image_byte))
    res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=5))
    res+='.jpg'
    image.save(os.path.join(os.path.join(os.path.dirname(__file__),'images'),res))