#!/usr/bin/python3
"""Export employee TODO list progress from JSONPlaceholder."""

import json
import sys
import urllib.request


def main():
    if len(sys.argv) != 2:
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        return

    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    try:
        with urllib.request.urlopen(users_url) as response:
            users = json.loads(response.read().decode("utf-8"))
    except Exception:
        return

    employee = None
    for user in users:
        if user.get("id") == employee_id:
            employee = user
            break

    if employee is None:
        return

    employee_name = employee.get("name")
    try:
        with urllib.request.urlopen(todos_url) as response:
            all_todos = json.loads(response.read().decode("utf-8"))
    except Exception:
        return

    todos = [todo for todo in all_todos if todo.get("userId") == employee_id]
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
