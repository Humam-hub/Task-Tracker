import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from tasks.json. If missing or invalid, return an empty list."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    """Save the tasks list to tasks.json using json.dump()."""
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")

def add_task(tasks):
    """Prompt for a task title, validate it, and append it as Pending."""
    title = input("Task title: ").strip()
    if not title:
        print("Error: Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    """Display all tasks with their 1-based index and Pending/Done status."""
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task.get("done", False) else "Pending"
        print(f"{index}. {task['title']} [{status}]")

def complete_task(tasks):
    """Mark a selected task as done."""
    if not tasks:
        print("No tasks to complete.")
        return
    
    choice = input("Task number: ").strip()
    try:
        task_num = int(choice)
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            save_tasks(tasks)
            print("Task completed.")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def delete_task(tasks):
    """Delete a selected task."""
    if not tasks:
        print("No tasks to delete.")
        return
    
    choice = input("Task number: ").strip()
    try:
        task_num = int(choice)
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{deleted['title']}' deleted.")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    tasks = load_tasks()
    
    print("--- TASK TRACKER ---")
    while True:
        print("1. Add  2. View  3. Complete  4. Delete  5. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()