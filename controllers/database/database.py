def get_posts():
    url = "https://fatal-bot-api.herokuapp.com/posts/"
    return requests.get(url)

def decrement_likes_post(post_id):
    url = "https://fatal-bot-api.herokuapp.com/posts/{}".format(post_id)
    return requests.get(url)
