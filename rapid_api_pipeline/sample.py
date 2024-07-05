

import requests
import json

url = "https://jsearch.p.rapidapi.com/search"

querystring = {"query":"Python developer in New-York,USA","page":"1","num_pages":"1"}

headers = {
	"x-rapidapi-key": "fedd9c56b2msh919589e6fe01d32p1d021djsna1b16e25b8a3",
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

with open("sample.json", "w") as f:
    data = response.json()["data"]
    json.dump(data, f, indent=4)

print("My response :")
#print(response.json())