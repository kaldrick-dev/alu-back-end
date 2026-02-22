#!/usr/bin/python3
"""Gather data from an API"""

import json
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
        user = json.loads(urlopen(f"https://jsonplaceholder.typicode.com/users/{user_id}").read())
        todos = json.loads(urlopen(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}").read())
    except Exception:
        sys.exit(1)

    name = user["name"]      
    done_count = sum(1 for t in todos if t["completed"])
    total = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(name, done_count, total))

    for task in todos:
        if task["completed"]:
            print("\t {}".format(task["title"]))