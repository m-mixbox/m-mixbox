import requests

url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/reverse"

querystring = {"lat":"23.317398","lon":"85.325524 ","zoom":"10","addressdetails":"1","namedetails":"0","accept-language":"en","format":"json","polygon_text":"0","polygon_kml":"0","polygon_svg":"0","polygon_geojson":"0","polygon_threshold":"0.0","limit":"1"}

headers = {
	"x-rapidapi-key": "0fc1cdd389msh5c2a73fb2c63065p15fb88jsnf7f07e4bb7f0",
	"x-rapidapi-host": "forward-reverse-geocoding.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())