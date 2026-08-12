import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1531944474287018125/  use your own"

message = input("Enter message: ")

payload = {
    "content": message
}

response = requests.post(WEBHOOK_URL, json=payload)

print(response.status_code)
