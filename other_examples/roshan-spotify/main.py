import requests
import json

print("Chicago art api call example")
id = input("Enter art id\n")

res = requests.get(f"https://api.artic.edu/api/v1/artworks/{id}")
res_json = res.json()

print('returned data:\n', res_json["data"]["thumbnail"])