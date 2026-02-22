#!/usr/bin/python3
"""Fetch and display an employee's TODO progress from JSONPlaceholder API."""

import json
import sys
from urllib import request


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    with request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ) as user_response:
        user = json.loads(user_response.read().decode("utf-8"))

    with request.urlopen(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    ) as todos_response:
        todos = json.loads(todos_response.read().decode("utf-8"))

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed") is True]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(done_tasks), len(todos)
        )
    )
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
