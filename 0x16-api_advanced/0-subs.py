#!/usr/bin/python3
"""
Function to query the Reddit API and return the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python:subreddit.counter:v1.0 (by /u/user)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
            else:
                return 0
        else:
            return 0
    except requests.RequestException:
        return 0
