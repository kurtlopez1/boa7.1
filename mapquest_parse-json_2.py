import urllib.parse
import requests

#API URL Address
main_api = "https://www.mapquestapi.com/directions/v2/route?" 

orig = "Rome, Italy"
dest = "Frascati, Italy"

#Generate key in the map API
key = "your_api_key"

#For API request
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

#Display Data From API URL
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")