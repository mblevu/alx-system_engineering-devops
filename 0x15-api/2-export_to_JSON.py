#!/usr/bin/python3

"""
This script fetches information about an employee's
TODO list progress from a REST API
and exports it to a JSON file.
"""
import json
import requests
import sys


def fetch_and_export_to_json(employee_id):
    """
    Fetches data from an API and exports it to a JSON file.

    Args:
        employee_id (int): The ID of the employee for whom the
    data needs to be fetched and exported.

    Returns:
        None: The function does not return any value. It only exports
    the data to a JSON file and prints a success message.
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

    tasks = []
    for todo in todos_data:
        task = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": employee_name
        }
        tasks.append(task)

    data = {employee_id: tasks}
    json_filename = f'{employee_id}.json'

    with open(json_filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
    print(f'Tasks exported to JSON file {json_filename}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        employee_id = sys.argv[1]
        fetch_and_export_to_json(employee_id)
