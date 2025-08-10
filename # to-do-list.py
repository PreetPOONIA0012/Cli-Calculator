# todo.py

import os

FILENAME = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter the task to add: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Cannot add empty task.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()