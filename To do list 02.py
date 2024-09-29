import os
import json

# File to store tasks
FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save tasks to file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)


def display_tasks(tasks):
    """Display all tasks with completion status."""
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task['completed'] else "Pending"
            print(f"{idx}. {task['name']} - [{status}]")


def add_task(tasks):
    """Add a new task."""
    task_name = input("\nEnter task name: ").strip()
    if task_name:
        tasks.append({"name": task_name, "completed": False})
        save_tasks(tasks)
        print(f"Task '{task_name}' added.")
    else:
        print("Task name cannot be empty!")


def mark_task(tasks, done=True):
    """Mark a task as done or undone."""
    try:
        task_num = int(input("\nEnter task number to mark as done/undone: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['completed'] = done
            status = "done" if done else "undone"
            print(f"Task '{tasks[task_num]['name']}' marked as {status}.")
            save_tasks(tasks)
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")


def remove_task(tasks):
    """Remove a task from the list."""
    try:
        task_num = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Task '{removed_task['name']}' removed.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")


def show_menu():
    """Display menu options."""
    print("\n=== To-Do List Application ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Mark Task as Undone")
    print("5. Remove Task")
    print("6. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task(tasks, done=True)
        elif choice == "4":
            mark_task(tasks, done=False)
        elif choice == "5":
            remove_task(tasks)
        elif choice == "6":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please choose a valid option.")


if __name__ == "__main__":
    main()
