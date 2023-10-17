import requests

def get_attachment_by_id(attachment_id):
    
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

    json_response = response.json()

    for post in json_response['posts']:
        for atttachment in post['attachments']:
            if atttachment.get('id') == attachment_id:
                return atttachment.get('title')

    return None

print(get_attachment_by_id(138))