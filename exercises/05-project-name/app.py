import requests

# your code here
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")

json_response = response.json()

print(json_response['name'])