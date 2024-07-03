import requests

lat = "23.317398"
long = "85.325524"
url = "https://nominatim.openstreetmap.org/reverse?format=geojson&lat="+lat+"&lon="+long

response = requests.get(url)

print(response.json())