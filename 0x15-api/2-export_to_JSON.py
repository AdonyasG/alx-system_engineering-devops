#!/usr/bin/python3
"""
Requests Data From API
Export to CSV
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users/" + argv[1])
    todo = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1])
    user = r.json().get("username")
    data = todo.json()
    userid = argv[1]
    dictt = {}
    dictt[userid] = []
    for i in data:
        dictt[userid].append({
            'task': i.get("title"),
            'completed': i.get("completed"),
            'username': user
            })
    with open(userid + ".json", 'w') as data_rec:
        json.dump(dictt, data_rec)
