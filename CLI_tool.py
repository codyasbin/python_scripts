#!/usr/bin/env python3
import sys
import requests

API_URL = "https://randomuser.me/api/"

# 1. Read CLI argument
arg = sys.argv[1] if len(sys.argv) > 1 else "all"

if arg=="--help":
    print("Usage: python CLI_tool.py [name|email|country|all]")
    sys.exit(0)
# 2. Call public API
response = requests.get(API_URL)
data = response.json()
user = data["results"][0]

name = f"{user['name']['first']} {user['name']['last']}"
email = user["email"]
country = user["location"]["country"]

# 3. Decide output based on CLI argument
if arg == "name":
    print(name)
elif arg == "email":
    print(email)
elif arg == "country":
    print(country)
else:
    print("Name   :", name)
    print("Email  :", email)
    print("Country:", country)