#!/usr/bin/python3
"""Script to export an employee's TODO list to a JSON file."""
import json
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

        tasks_list = []
        for task in todos_res:
            tasks_list.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            })

        data = {user_id: tasks_list}

        with open("{}.json".format(user_id), mode="w") as f:
            json.dump(data, f)
