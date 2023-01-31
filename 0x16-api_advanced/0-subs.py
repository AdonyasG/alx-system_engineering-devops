#!/usr/bin/python3
"""
Requests Data From API
"""

import requests


def number_of_subscribers(subreddit):
    """find number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = requests.utils.default_headers()
    headers.update(
                   {
                       'User-Agent': 'User Agent 1.0',
                    }
                  )
    response = requests.get(url, headers=headers).json()
    subs = response.get('data', {}).get('subscribers')

    if subs:
        return subs
    else:
        return 0
