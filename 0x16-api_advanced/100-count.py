#!/usr/bin/python3
"""100-count-parses the title of all hot articles, and prints a sorted
count of given keywords (case-insensitive, delimited by spaces"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    headers = {"User-Agent": 'Mozilla/5.0'}
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
        title = child.get('data').get('title')
        for word in word_list:
            if word.lower() in title.lower():
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    after = data.get('after')
    if after:
        return count_words(subreddit, word_list, after, word_count)
    else:
        if len(word_count) == 0:
            return
        for key, value in sorted(word_count.items(),
                                 key=lambda item: item[1], reverse=True):
            print("{}: {}".format(key, value))
