import requests

# your code here
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")

json_response = response.json()

print(json_response[-1]['images'][-1])