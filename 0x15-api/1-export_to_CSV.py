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

    try:
        user = requests.get(user_url).json()
        todos = requests.get(todos_url).json()