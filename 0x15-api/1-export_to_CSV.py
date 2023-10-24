#!/usr/bin/python3
"""
This script fetches and displays information about
an employee's TODO list progress
from a REST API and exports the data in CSV format.
"""
import csv
import requests
import sys


def fetch_and_export_to_csv(employee_id):
    """Fetches employee TODO list progress
    from a REST API and exports the data in CSV format.
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = base_url + 'users/{}'.format(employee_id)
    todos_url = base_url + 'todos?userId={}'.format(employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_id = user_data.get('id')
    employee_name = user_data.get('name')

    csv_file_name = '{}.csv'.format(employee_id)

    completed_tasks = [
        {
            "USER_ID": employee_id,
            "USERNAME": employee_name,
            "TASK_COMPLETED_STATUS": todo.get('completed'),
            "TASK_TITLE": todo.get('title')
        }
        for todo in todos_data
    ]

    with open(csv_file_name, mode='w') as csv_file:
        fieldnames = [
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        ]
        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
            quoting=csv.QUOTE_ALL)
        for task in completed_tasks:
            writer.writerow(task)
        print("Data exported to {}".format(csv_file_name))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_id = sys.argv[1]
        fetch_and_export_to_csv(employee_id)
