#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress and export in CSV"""
import csv
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

    username = data[0]["user"]["username"]

    with open(f"{EMPLOYEE_ID}.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for task in data:
            writer.writerow(
                [EMPLOYEE_ID, username, str(task["completed"]), task["title"]]
            )