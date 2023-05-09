#!/usr/bin/python3
"""
a recursive function that queries the reddit API and returns
a list of all hot articles for a given subtree
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns the hot articles of subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    params = {"after": after} if after else None
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 404:
        return None
    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        hot_list.append(post["data"]["title"])
    after = data["data"]["after"]
    if after:
        recurse(subreddit, hot_list, after=after)
    return hot_list
