#!/usr/bin/python3
"""
Requests Data From API
"""

import requests


def top_ten(subreddit):
    """find number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = requests.utils.default_headers()
    headers.update(
                   {
                       'User-Agent': 'User Agent 1.0',
                    }
                  )
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    post = response.get('data', {}).get('children', [])
    if post:
        for i in post:
            print(i.get('data').get('title'))
    else:
        print(None)
