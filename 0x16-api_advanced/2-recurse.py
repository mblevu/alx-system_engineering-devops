#!/usr/bin/python3
"""2-recurse-recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Retrieves the titles of the hot posts from a given subreddit on Reddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve hot posts from.
        hot_list (list, optional): A list to store the titles of the hot posts.
        Defaults to an empty list.
        after (str, optional): The identifier of the last post retrieved.
        Defaults to None.

    Returns:
        list: A list containing the titles of the hot posts from the given
        subreddit.
    """
    headers = {"User-Agent": 'mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get('data')
    if not data:
        return None
    for child in data.get('children', []):
        hot_list.append(child.get('data').get('title'))
    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
