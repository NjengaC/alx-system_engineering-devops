#!/usr/bin/python3
"""
Module returns the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given, the function returns 0
"""
import requests


def number_of_subscribers(subreddit):
    """ Function returns a list of subscibers for a certain subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 \
            Mobile Safari/537.36"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200 and 'data' in response.json():
        return response.json()['data']['subscribers']
    else:
        return 0
