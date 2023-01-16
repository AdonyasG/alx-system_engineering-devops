#!/usr/bin/python3
"""export to json format"""

import json
import requests


if __name__ == "__main__":
    all_users = requests.get("https://jsonplaceholder.typicode.com/users")
    all_users_list = all_users.json()
    map = {}
    for user in all_users_list:
        map[user.get("id")] = user.get("username")

    all_tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    all_tasks_list = all_tasks.json()

    data = {}
    user_id = 0
    for task in all_tasks_list:
        if user_id != task.get("userId"):
            user_id = task.get("userId")
            data[user_id] = []
        data[user_id].append({
            'task': task.get("title"),
            'completed': task.get("completed"),
            'username': map.get(user_id)
        })

    with open("todo_all_employees.json", "w") as out:
        json.dump(data, out)
