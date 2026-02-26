#!/usr/bin/python3
"""Export employee TODO data from API to a CSV file."""

import csv
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

    file_content = []
    for todo in response.json():
        file_content.append(
            [
                str(user_id),
                user_name,
                todo.get("completed"),
                todo.get("title"),
            ]
        )

    file_name = "{}.csv".format(user_id)
    with open(file_name, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for row in file_content:
            csv_writer.writerow(row)


if __name__ == "__main__":
    main()
