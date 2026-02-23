#!/usr/bin/python3
"""Export all employees TODO lists to JSON."""

import json
from urllib.request import urlopen


if __name__ == "__main__":
    users = json.loads(
        urlopen("https://jsonplaceholder.typicode.com/users", timeout=10).read()
    )
    todos = json.loads(
        urlopen("https://jsonplaceholder.typicode.com/todos", timeout=10).read()
    )

    users_by_id = {user["id"]: user["username"] for user in users}
    data = {}

    for task in todos:
        uid = task["userId"]
        key = str(uid)
        if key not in data:
            data[key] = []
        data[key].append(
            {
                "username": users_by_id[uid],
                "task": task["title"],
                "completed": task["completed"],
            }
        )

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)
