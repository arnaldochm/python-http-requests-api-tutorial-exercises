import requests

# your code here
response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

json_response = response.json()

print(json_response['posts'][0]['author']['name'])