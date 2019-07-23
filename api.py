import requests

response = requests.get("https://freegeoip.app/json")
print(response.json())
