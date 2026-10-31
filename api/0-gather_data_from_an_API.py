#!/usr/bin/python3
"""Script that returns information about an employee's TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com"
        user_res = requests.get("{}/users/{}".format(url, user_id)).json()
        todos_res = requests.get("{}/todos?userId={}".format(
            url, user_id)).json()

        name = user_res.get("name")
        done_tasks = [t for t in todos_res if t.get("completed") is True]

        print("Employee {} is done with tasks({}/{}):".format(
            name, len(done_tasks), len(todos_res)))

        for task in done_tasks:
            print("\t {}".format(task.get("title")))
