import requests

base_url = "https://api.upcitemdb.com/prod/trial/lookup"
parameters = {"upc": "885909950805"}

response = requests.get(base_url, params= parameters)

print(response.url)