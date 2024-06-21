import requests


key = "test"
value = "test2"

url = f"http://localhost:8000/set/{key}"
payload = {"value": value}
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers)

get_url = f"http://localhost:8000/set/{key}"
requests.delete(url)