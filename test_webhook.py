import requests


user_message =  "Can you tell me about blach holes in 3-4 lines"

request_message = {"message" : user_message}

url = "PASTE_YOUR_WEBHOOK_URL"

response = requests.post(url, json=request_message)

print(response.status_code)

print("Response:",response.text)
