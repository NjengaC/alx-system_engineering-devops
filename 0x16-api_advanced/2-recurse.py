#!/usr/bin/python3
"""Recursively fetches titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches titles of all hot articles for a given subreddit."""
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {'User-Agent': 'MyBot/0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200 and 'data' in response.json():
        posts = response.json()['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        after = response.json()['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
