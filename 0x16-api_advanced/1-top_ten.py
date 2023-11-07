#!/usr/bin/python3
"""1-top_ten-queries the Reddit API and prints the titles
of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        for post in response.json()["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
