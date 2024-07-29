import requests
import sys
import json
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

##print(json.dumps(response.json(),indent=2))
if len(sys.argv)!= 2:
    sys.exit("Missing command-line argument")

if sys.argv[1].isalpha():
    sys.exit("Commnad line argument is not a number")

o = response.json()

rate_float = o["bpi"]["USD"]["rate_float"]

rate_float = rate_float * float(sys.argv[1])
formatted_value = f"{rate_float:,.2f}"  

print("$",formatted_value,sep="")
