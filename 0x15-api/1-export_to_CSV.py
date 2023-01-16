#!/usr/bin/python3
"""
Requests Data From API
Export to CSV
"""

import csv
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
    with open(userid + ".csv", 'w') as data_rec:
        for i in data:
            data_status = i.get("completed")
            title = i.get("title")
            formatt = csv.writer(data_rec, delimiter=',', quotechar='"',
                                 quoting=csv.QUOTE_ALL)
            formatt.writerow([str(userid), str(user), str(data_status),
                              str(title)])
