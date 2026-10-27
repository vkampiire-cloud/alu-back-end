#!/usr/bin/python3
"""Script to export an employee's TODO list to a CSV file."""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com"
        user_res = requests.get("{}/users/{}".format(url, user_id)).json()
        todos_res = requests.get("{}/todos?userId={}".format(
            url, user_id)).json()

        username = user_res.get("username")

        with open("{}.csv".format(user_id), mode="w", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in todos_res:
                writer.writerow([
                    user_id,
                    username,
                    task.get("completed"),
                    task.get("title")
                ])
