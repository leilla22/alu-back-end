#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress and export in JSON"""
import json
import sys
from urllib import request, parse


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    API_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    url = f"{API_URL}/users/{EMPLOYEE_ID}/todos"
    url = url + "?" + parse.urlencode({"_expand": "user"})
    with request.urlopen(url) as resp:
        data = json.load(resp)

    if not len(data):
        print("RequestError:", 404)
        sys.exit(1)

    user_tasks = {EMPLOYEE_ID: []}
    for task in data:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": task["user"]["username"]
        }
        user_tasks[EMPLOYEE_ID].append(task_dict)

    with open(f"{EMPLOYEE_ID}.json", "w") as file:
        json.dump(user_tasks, file)