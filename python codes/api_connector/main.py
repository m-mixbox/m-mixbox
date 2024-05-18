import requests
import json
#api_url = "http://localhost/flutter_login/check.php"
api_url = "https://mixboxsolutions.com/api_test/check.php"
data = {"email": "a@gmail.com", "password": "@ADMIN#1234"}
headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, headers=headers,data = json.dumps(data))
if(response.status_code == 200):
    print(json.dumps(response.json(), indent=4, sort_keys=True))
else :
    print(response.status_code)