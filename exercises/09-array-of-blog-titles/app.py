import requests

def get_titles():
    # your code here
    titles = []

    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

    json_response = response.json()

    for post in json_response['posts']:
        titles.append(post['title'])

    return titles


print(get_titles())