#!/usr/bin/python3
'''
Prints the titles of the first 10 hot posts for a given subreddit
'''
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {'User-Agent': 'MyBot/0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200 and 'data' in response.json():
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print("None")
