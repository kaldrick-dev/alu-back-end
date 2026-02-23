#!/usr/bin/python3
"""Export an employee TODO list to CSV."""

import csv
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

    file_name = "{}.csv".format(user_id)
    with open(file_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                [
                    user_id,
                    user["username"],
                    task["completed"],
                    task["title"],
                ]
            )
