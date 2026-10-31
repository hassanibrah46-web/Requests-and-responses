import requests

url = "https://jsonplaceholder.typicode.com/users/1"

responses= requests.get(url, timeout=10)
if responses.status_code == 200:
    user = responses.json()

    print("name:", user['name'])
    print("email:", user['email'])
    print("city:", user['address']['city'])
else:
    print("Request failed:", responses.status_code)

