#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress
from https://jsonplaceholder.typicode.com
"""

import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee info
    user_resp = requests.get(f"{base_url}/users/{employee_id}")
    if user_resp.status_code != 200:
        sys.exit(1)

    user = user_resp.json()
    user_id = user.get("id")
    username = user.get("username")

    # Fetch todos
    todos_resp = requests.get(f"{base_url}/todos",
                              params={"userId": employee_id})
    if todos_resp.status_code != 200:
        sys.exit(1)

    todos = todos_resp.json()

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    filename = f"{user_id}.json"
    data = {str(user_id): tasks}

    with open(filename, mode="w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)

if __name__ == "__main__":
    main()