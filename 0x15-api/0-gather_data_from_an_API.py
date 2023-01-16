#!/usr/bin/python3
"""
Requests Data From API
"""

import json
import requests
from sys import argv


def information():
    """return info from api"""
    r = requests.get("https://jsonplaceholder.typicode.com/users")
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = r.text
    datas = todo.text
    parse = json.loads(data)
    parses = json.loads(datas)
    TOTAL_NUM_OF_TASKS = 0
    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    for i in parse:
        if i.get('id') == int(argv[1]):
            EMPLOYEE_NAME = (i.get('name'))
            break
    for i in parses:
        if i.get('userId') == int(argv[1]):
            TOTAL_NUM_OF_TASKS += 1
            if i.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(i.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for i in TASK_TITLE:
        print("\t {}".format(i))


if __name__ == "__main__":
    information()
