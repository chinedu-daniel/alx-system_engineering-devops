#!/usr/bin/python3
"""
Retrieves and displays the TODO list progress for a given employee ID
using a REST API.
"""
import requests
import sys


def get_employee_todo_list(em_id):

    """
    Retrieve and display the TODO list progress for a given employee ID.
    Args:
        employee_id (int): The ID of the employee.
    """

    url = "https://jsonplaceholder.typicode.com"

    # Get employee details
    user_response = requests.get(f"{url}/users/{em_id}")
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get employee's TODO list
    todos_response = requests.get(f"{url}/todos", params={"userId": em_id})
    todos = todos_response.json()

    # Calculate the TODO list progress
    done_tasks = [todo for todo in todos if todo.get("completed")]
    total = len(todos)
    done = len(done_tasks)

    # Display the TODO list progress
    print(f"Employee {employee_name} is done with tasks({done}/{total}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo_list_progress.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_list(employee_id)
