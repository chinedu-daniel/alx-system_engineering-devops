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
    req = requests.get(
        "https://www.reddit.com/r/{subreddit}/about.json".format(subreddit),
        headers={'User-Agent': "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
