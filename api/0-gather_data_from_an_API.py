#!/usr/bin/python3
"""Gather data from an API."""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])

        user_resp = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}",
            timeout=10,
        )
        todos_resp = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={user_id}",
            timeout=10,
        )
        user_resp.raise_for_status()
        todos_resp.raise_for_status()

        user = user_resp.json()
        todos = todos_resp.json()
    except Exception:
        sys.exit(1)

    done_tasks = [task for task in todos if task.get("completed") is True]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"),
            len(done_tasks),
            len(todos),
        )
    )

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
