import urllib.parse
import requests

#API URL Address
main_api = "https://www.mapquestapi.com/directions/v2/route?" 

orig = "Washington, D.C."
dest = "Baltimore, Md"

#Generate key in the map API
key = "your_api_key"

#For API request
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

#Display Data From API URL
json_data = requests.get(url).json()
print(json_data)