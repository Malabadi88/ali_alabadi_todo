import sys
import os

def display_tasks(tasks):
    """
    Displays the current list of tasks.
    """
    if not tasks:
        print("Your to-do list is empty. Add a new task to get started!")
        return

    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task.startswith("[✓]") else " "
        task_text = task.replace("[✓]", "").strip()
        print(f"{i}. [{status}] {task_text}")
    print("-----------------------\n")

def add_task(tasks, new_task_text):
    """
    Adds a new task to the list.
    """
    tasks.append(f"[ ] {new_task_text}")
    print(f"Task added: '{new_task_text}'")

def complete_task(tasks, task_index):
    """
    Marks a task as complete.
    """
    try:
        task_index = int(task_index) - 1
        if 0 <= task_index < len(tasks):
            task = tasks[task_index]
            if not task.startswith("[✓]"):
                tasks[task_index] = "[✓]" + task.lstrip("[ ]").lstrip()
                print(f"Task '{tasks[task_index].replace('[✓]', '').strip()}' marked as complete.")
            else:
                print("Task is already complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks, task_index):
    """
    Deletes a task from the list.
    """
    try:
        task_index = int(task_index) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index).replace("[✓]", "").strip()
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def load_tasks(filepath="tasks.txt"):
    """
    Loads tasks from the specified file.
    """
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_tasks(tasks, filepath="tasks.txt"):
    """
    Saves tasks to the specified file.
    """
    with open(filepath, 'w') as f:
        for task in tasks:
            f.write(f"{task}\n")

def main():
    """
    The main function for the to-do list application.
    """
    tasks = load_tasks()

    while True:
        display_tasks(tasks)
        print("Options: add <task>, complete <number>, delete <number>, quit")
        command_parts = input("Enter a command: ").split(' ', 1)
        command = command_parts[0].lower()
        args = command_parts[1] if len(command_parts) > 1 else None

        if command == 'add' and args:
            add_task(tasks, args)
        elif command == 'complete' and args:
            complete_task(tasks, args)
        elif command == 'delete' and args:
            delete_task(tasks, args)
        elif command == 'quit':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
