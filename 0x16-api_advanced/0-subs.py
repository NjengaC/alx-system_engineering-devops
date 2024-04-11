#!/usr/bin/python3
"""Counts number of subs"""
import requests


def number_of_subscribers(subreddit=None):
    """Function to retrieve the number of subscribers for a given subreddit"""

    if not subreddit or not isinstance(subreddit, str):
        return 0

    try:
        result = requests.get('http://www.reddit.com/r/{}/about.json'.
                              format(subreddit),
                              headers={'User-Agent': 'mycoolapp/1.0'})
        result.raise_for_status()
        data = result.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers
    except Exception:
        return 0
