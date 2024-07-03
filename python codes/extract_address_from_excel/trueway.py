import requests

url = "https://trueway-geocoding.p.rapidapi.com/ReverseGeocode"

querystring = {"location":"23.317398,85.325524","language":"en"}

headers = {
	"x-rapidapi-key": "0fc1cdd389msh5c2a73fb2c63065p15fb88jsnf7f07e4bb7f0",
	"x-rapidapi-host": "trueway-geocoding.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json()["results"][0]["address"])