#!/usr/bin/python3
"""Count words in subreddit titles"""
import json
import requests


def count_words(subreddit, word_list, after=None, word_dict={}):
    """Count words in subreddit titles"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    if not word_dict:
        for word in word_list:
            word_dict[word.lower()] = 0
    data = response.json()
    for post in data.get('data').get('children'):
        title = post.get('data').get('title').lower().split()
        for word in title:
            if word in word_dict:
                word_dict[word] += 1
    after = data.get('data').get('after')
    if after:
        return count_words(subreddit, word_list, after, word_dict)
    else:
        for word in sorted(word_dict, key=word_dict.get, reverse=True):
            if word_dict[word] > 0:
                print('{}: {}'.format(word, word_dict[word]))
