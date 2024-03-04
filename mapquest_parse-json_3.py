import urllib.parse
import requests

#API URL Address
main_api = "https://www.mapquestapi.com/directions/v2/route?" 

#Generate key in the map API
key = "fZadaFOY22VIEEemZcBFfxl5vjSXIPpZ"

#For API request
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

#Display Data From API URL With User Input for Origin and Destination
while True:
   orig = input("Starting Location: ")
   dest = input("Destination: ")
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
