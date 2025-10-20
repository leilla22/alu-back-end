#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress"""
import sys
from urllib import request, parse
import json


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

    employee_name = data[0]["user"]["name"]
    total_tasks = len(data)
    done_tasks = [task for task in data if task["completed"]]
    total_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks"
          f"({total_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")