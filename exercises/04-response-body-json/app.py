import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")

json_response = response.json()

print(f"Current time: {json_response['hours']} hrs {json_response['minutes']} min and {json_response['seconds']} sec")

