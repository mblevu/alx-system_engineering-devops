#!/usr/bin/python3
"""
This script fetches and displays information about
an employee's TODO list progress
from a REST API and exports the data in CSV format.
"""
import csv
import requests
import sys


def fetch