#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress from JSONPlaceholder API.
"""

import json
import sys
from urllib import request, error


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer", file=sys.stderr)
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    try:
        # Get user info
        with request.urlopen(f"{base_url}/users/{employee_id}") as user_resp:
            if user_resp.getcode() != 200:
                raise ValueError("User not found")
            user = json.loads(user_resp.read().decode("utf-8"))

        # Get todos
        with request.urlopen(f"{base_url}/todos?userId={employee_id}") as todos_resp:
            if todos_resp.getcode() != 200:
                raise ValueError("Todos not found")
            todos = json.loads(todos_resp.read().decode("utf-8"))

    except (error.HTTPError, error.URLError) as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        print(f"Error processing response: {e}", file=sys.stderr)
        sys.exit(1)

    name = user.get("name", "Unknown Employee")
    done_tasks = [task for task in todos if task.get("completed") is True]

    total = len(todos)
    done = len(done_tasks)

    print(f"Employee {name} is done with tasks({done}/{total}):")

    for task in done_tasks:
        title = task.get("title", "Untitled task")
        # Exactly: tab character + one space + title
        print("\t " + title)


if __name__ == "__main__":
    main()