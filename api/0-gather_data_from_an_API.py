#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress.
"""

import sys
import json
import urllib.request


def main():
    if len(sys.argv) != 2:
        return

    employee_id = int(sys.argv[1])

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"

    try:
        with urllib.request.urlopen(user_url) as response:
            user = json.loads(response.read().decode("utf-8"))
    except Exception:
        return

    employee_name = user.get("name")

    todos_url = f"{base_url}/todos?userId={employee_id}"
    try:
        with urllib.request.urlopen(todos_url) as response:
            todos = json.loads(response.read().decode("utf-8"))
    except Exception:
        return

    total_tasks = len(todos)
    completed_tasks = [t for t in todos if t.get("completed") is True]
    done_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done "
        f"with tasks({done_tasks}/{total_tasks}):"
    )

    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    main()
