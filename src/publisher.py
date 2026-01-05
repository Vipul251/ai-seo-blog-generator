import requests

def publish_to_wordpress(title, content):
    url = "https://your-site.com/wp-json/wp/v2/posts"
    auth = ("username", "application_password")

    data = {
        "title": title,
        "content": content,
        "status": "publish"
    }

    requests.post(url, auth=auth, json=data)
