import requests


user_message =  "Can you tell me about blach holes in 3-4 lines"

request_message = {"message" : user_message}

url = "https://vaidhika-11.app.n8n.cloud/webhook/63c04f9d-3c81-48f9-88b9-7ea1f52291db"

response = requests.post(url, json=request_message)

print(response.status_code)

print("Response:",response.text)