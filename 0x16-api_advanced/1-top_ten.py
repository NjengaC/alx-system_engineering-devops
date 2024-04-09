#!/usr/bin/python3
"""Fetches the top 10 hottest posts from a Reddit API endpoint."""

import requests
import sys


def top_ten(subreddit):
    """Fetches the top 10 hottest posts from a specified subreddit.

    Args:
        subreddit (str): The subreddit to fetch posts from.

    Returns:
        None: If an invalid subreddit is provided or if there are no posts.
        List[str]: The titles of the top 10 hottest posts.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 10}
    headers = {'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    # Check if subreddit is provided and is a string
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        sys.exit()

    try:
        # Send GET request to Reddit API
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        # Extract data from response
        data = response.json().get("data")
        posts = data.get("children")

        # Extract titles of top 10 posts
        titles = [post.get("data").get("title") for post in posts]

        # Print titles of top 10 posts
        [print(title) for title in titles]
    except Exception:
        print("None")
