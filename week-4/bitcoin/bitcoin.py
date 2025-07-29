import requests
import json
import sys


data = requests.get(
    "https://rest.coincap.io/v3/assets/bitcoin?apiKey=c42acd8cab0972867f68347807b2f591b1c851bc26922be7ce7eb3f828efd558"
)
#data ke json e convert korte hbe
data_dict = data.json()
# then 
price = data_dict["data"]["priceUsd"]
try:
    total_price = float(price) * float(sys.argv[1])
    print(f"${total_price:,.4f}")
except ValueError:
    sys.exit("Provide a number")

#data ke json e convert korte hbe