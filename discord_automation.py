import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1531944474287018125/iY7zvc6ZvDaggGJ8lbB673iXnD_ac1ChN_M5SlAxvUo8C6WeYlbMKuCerhOkRan82wes"

message = input("Enter message: ")

payload = {
    "content": message
}

response = requests.post(WEBHOOK_URL, json=payload)

print(response.status_code)