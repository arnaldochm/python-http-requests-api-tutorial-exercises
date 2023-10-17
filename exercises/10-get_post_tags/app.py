import requests

def get_post_tags(post_id):
    # your code here
    tags = []

    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

    json_response = response.json()

    post_by_id = [post for post in json_response['posts'] if post.get('id') == post_id]

    return post_by_id[0]['tags']
    


print(get_post_tags(135))