#!/usr/bin/python3
"""Export employee TODO data from API to a JSON file."""

import json
import requests
import sys


def main():
    """Main function."""
    if len(sys.argv) != 2:
        return

    user_id = int(sys.argv[1])
    todo_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    )
    user_url = (
        "https://jsonplaceholder.typicode.com/users?id={}".format(user_id)
    )

    response = requests.get(todo_url)
    user_response = requests.get(user_url)
    users = user_response.json()
    if not users:
        return

    user_name = users[0].get("username")
    user_data = []
    output = {str(user_id): user_data}

    for todo in response.json():
        user_data.append(
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user_name,
            }
        )

    file_name = "{}.json".format(user_id)
    with open(file_name, "w") as file:
        json.dump(output, file)


if __name__ == "__main__":
    main()
