#!/usr/bin/python3
"""Export all employees TODO data from API to a JSON dictionary."""

import json
import requests


def main():
    """Main function."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todo_url)

    usernames = {}
    for user in users_response.json():
        usernames[user.get("id")] = user.get("username")

    output = {}

    for todo in todos_response.json():
        user_id = todo.get("userId")
        user_id_str = str(user_id)
        if user_id_str not in output:
            output[user_id_str] = []

        output[user_id_str].append(
            {
                "username": usernames.get(user_id),
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
        )

    with open("todo_all_employees.json", "w") as file:
        json.dump(output, file)


if __name__ == "__main__":
    main()
