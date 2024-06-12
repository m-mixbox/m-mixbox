import requests
from requests.structures import CaseInsensitiveDict
import json

url = "https://api.geoapify.com/v1/geocode/reverse?lat=23.3499431&lon=85.3245952&apiKey=b03147987fd74ef7bc077ae9d31f2642"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

resp = requests.get(url, headers=headers)

with open('data.json', 'w') as f:
    json.dump(resp.json(), f)