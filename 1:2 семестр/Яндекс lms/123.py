import requests
import pprint

response = requests.get(url="https://api.github.com")
# print(response.status_code)
# print(response.text)
response_json = response.json()
pprint.pprint(object=response_json)
