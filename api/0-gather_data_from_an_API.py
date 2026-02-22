#!/usr/bin/python3
"""Gather data from an API."""

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

    done_tasks = [task for task in todos if task.get("completed") is True]

    lines = []
    lines.append(
        "Employee {} is done with tasks({}/{}):".format(
            user["name"],
            len(done_tasks),
            len(todos),
        )
    )
    for task in done_tasks:
        lines.append("\t {}".format(task.get("title")))

    output = "\n".join(lines) + "\n"

    sys.stdout.write(output)

    with open("student_output", "w") as f:
        f.write(output)