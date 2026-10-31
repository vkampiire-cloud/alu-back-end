#!/usr/bin/python3
"""Script to export all tasks from all employees to a JSON file."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(url)).json()
    todos = requests.get("{}/todos".format(url)).json()

    all_data = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        user_tasks = []
        for task in todos:
            if str(task.get("userId")) == user_id:
                user_tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
        all_data[user_id] = user_tasks

    with open("todo_all_employees.json", mode="w") as f:
        json.dump(all_data, f)
