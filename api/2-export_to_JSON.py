#!/usr/bin/python3
"""Export an employee TODO list to JSON."""

import json
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
        user = json.loads(
            urlopen(
                "https://jsonplaceholder.typicode.com/users/{}".format(user_id),
                timeout=10,
            ).read()
        )
        todos = json.loads(
            urlopen(
                "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                    user_id
                ),
                timeout=10,
            ).read()
        )
    except Exception:
        sys.exit(1)

    data = {
        str(user_id): [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user["username"],
            }
            for task in todos
        ]
    }

    file_name = "{}.json".format(user_id)
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)
