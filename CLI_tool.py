# user_cli.py
import requests

API_URL = "https://randomuser.me/api/"

response = requests.get(API_URL)

data = response.json()

user = data["results"][0]

name = f"{user['name']['first']} {user['name']['last']}"
email = user["email"]
country = user["location"]["country"]

print("👤 Name   :", name)
print("📧 Email  :", email)
print("🌍 Country:", country)