#!/usr/bin/python3
"""
Module returns the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given, the function returns 0
"""
import requests


def number_of_subscribers(subreddit):
    """ Function returns a list of subscibers for a certain subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/about.json "

    headers = {'User-Agent': 'MyBot/0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200 and 'data' in response.json():
        return response.json()['data']['subscribers']
    else:
        return 0
