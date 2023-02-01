#!/usr/bin/python3
"""
Requests Data from an API
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns count of hotlist"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'User agent- 1.0'}
    params = {'limit': 100, 'after': after}
    r = requests.get(url, headers=headers,
                     params=params, allow_redirects=False)
    if r.status_code == 200:
        data = r.json().get('data')
        after = data.get('after')
        children = data.get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
