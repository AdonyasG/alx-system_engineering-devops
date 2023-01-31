#!/usr/bin/python3
"""
Requests Data From API
"""

import requests


def recurse(subreddit, hot_list=[], after="aft"):
    """find number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = requests.utils.default_headers()
    headers.update(
                   {
                       'User-Agent': 'User Agent 1.0',
                    }
                  )
    if after != "aft":
        url = url + "?after={}".format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)
    post = response.json().get('data', {}).get('children', [])

    if not post:
        return hot_list
    for i in post:
        hot_list.append(i.get('data').get('title'))

    after = response.json().get('data').get('after')

    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))
