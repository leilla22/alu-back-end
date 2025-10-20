#!/usr/bin/python3
"""Script to use a REST API, returns information about
all tasks from all employees and export in JSON"""
import json
from urllib import request


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"

    with request.urlopen(f"{API_URL}/users") as resp:
        users = json.load(resp)

    dict_users_tasks = {}
    for user in users:
        with request.urlopen(f"{API_URL}/users/{user['id']}/todos") as resp:
            tasks = json.load(resp)

        dict_users_tasks[user["id"]] = []
        for task in tasks:
            task_dict = {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            dict_users_tasks[user["id"]].append(task_dict)

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict_users_tasks, file)