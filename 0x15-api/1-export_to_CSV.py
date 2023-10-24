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
    """
    Fetches a to-do list for a given employee from a REST API
    and exports the data in CSV format.

    Args:
        employee_id (int): The ID of the employee for whom the
        to-do list is to be fetched.

    Returns:
        None

    Exports the employee's name, the number of completed tasks,
    and the titles of the completed tasks to a CSV file named
    <employee_id>.csv.
    """

    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = base_url + 'users/{}'.format(employee_id)
    todo_url = base_url + 'todos?userId={}'.format(employee_id)

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)
    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_id = user_data.get('id')
    employee_name = user_data.get('name')

    completed_tasks = [
        (employee_id, employee_name,
            str(todo.get('completed')),
            todo.get('title'))
            for todo in todo_data
            ]

    csv_filename = f'{employee_id}.csv'

    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(completed_tasks)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        employee_id = sys.argv[1]
        fetch_and_export_to_csv(employee_id)
