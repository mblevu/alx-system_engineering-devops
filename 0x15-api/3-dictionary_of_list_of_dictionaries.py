#!/usr/bin/python3

"""
This script fetches information about all employees' TODO list progress from a REST API
and exports it to a JSON file.
"""
import json
import requests


def fetch_and_export_to_json():
    """
    Fetches data from an API and exports it to a JSON file.

    Retrieves user data from the "https://jsonplaceholder.typicode.com/users"
    endpoint and then retrieves the corresponding to-do tasks for each user
    from the "/{user_id}/todos" endpoint. It organizes the tasks by user and
    exports the data to a JSON file named "todo_all_employees.json".

    Example Usage:
    fetch_and_export_to_json()

    Inputs:
    There are no inputs for this function.

    Outputs:
    The function does not return any output. It exports the tasks data for all
    users to a JSON file named "todo_all_employees.json".
    """

    base_url = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(base_url)
    users_data = users_response.json()

    all_data = {}
    for user in users_data:
        employee_id = user.get('id')
        employee_name = user.get('username')
        todos_url = base_url + '/{}/todos'.format(employee_id)
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        tasks = []
        for todo in todos_data:
            task = {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": employee_name
            }
            tasks.append(task)

        all_data[employee_id] = tasks

    json_filename = 'todo_all_employees.json'

    with open(json_filename, 'w') as jsonfile:
        json.dump(all_data, jsonfile, indent=4)


if __name__ == '__main__':
    fetch_and_export_to_json()
