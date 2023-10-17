import requests

# your code here
import requests
url = 'https://assets.breatheco.de/apis/fake/sample/post.php'
myobj = {'somekey': 'somevalue'}

response = requests.post(url, json = myobj)

print(response.text)