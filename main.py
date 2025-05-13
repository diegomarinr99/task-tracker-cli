import argparse
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the file if it exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks():
    """Save current task to the file."""
    with open (TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# This will store tasks temporarily
tasks = load_tasks()

def add_task(task):
    """Add a task to the list."""
    if any(t["description"].lower() == task.lower() for t in tasks):
        print(f"Task already exists: {task}")
        return
    tasks.append({"description": task, "done": False})
    save_tasks()
    print(f"Task added: {task}")

def list_tasks(args):
    """List all tasks."""
    if not tasks:
        print("No tasks available.")
    # elif args.done:
    #     for idx, task in enumerate(tasks, 1):
    #         if not task['done']:
    #             continue
    #         else:
    #             status = "✔"
    #             print(f"{idx}. [{status}] {task['description']}")
    # elif args.pending:
    #     for idx, task in enumerate(tasks, 1):
    #         if task['done']:
    #             continue
    #         else:
    #             status = ""
    #             print(f"{idx}. [{status}] {task['description']}")
    # else:
    #     for idx, task in enumerate(tasks, 1):
    #         status = "✔" if task['done'] else ""
    #         print(f"{idx}. [{status}] {task['description']}")
    for idx, task in enumerate(tasks,1):
        if args.done and not task['done']:
            continue
        elif args.pending and task['done']:
            continue
        status = "✔" if task['done'] else ""
        print(f"{idx}. [{status}] {task['description']}")

def delete_task(index):
    """Delete a task in specific index"""
    if not tasks:
        print("No tasks to delete")
    elif index < 1 or index > len(tasks):
        print(f"Invalid index: {index}")
    else:
        del tasks[index-1]
        print(f"Task {index} deleted successfully")
        save_tasks()

def mark_done(index):
    """Mark a task as done"""
    if not tasks:
        print("No tasks to mark as done")
    elif index < 1 or index > len(tasks):
        print(f"Invalid index: {index}")
    else:
        task = tasks[index -1]
        status = task['done']
        if status:
            print(f"Task {task['description']} is already marked as done.")
        else:
            task['done'] = True
            print(f"Task {task['description']} has been marked as done.")
            save_tasks()

def mark_undone(index):
    """Unmark a done task"""
    if not tasks:
        print("No tasks to set as undone")
    elif index < 1 or index > len(tasks):
        print(f"Invalid index: {index}")
    else:
        task = tasks[index -1]
        status = task['done']
        if not status:
            print(f"Task {task['description']} is already marked as undone.")
        else:
            task['done'] = False
            print(f"Task {task['description']} has been marked as undone.")
            save_tasks()

def clear_tasks():
    confirm = input("Are you sure you want to delete all tasks? This CANNOT be undone (y/n): ")
    if confirm.lower() == 'y':
        tasks.clear()
        save_tasks()
        print("All tasks have been cleared.")
    else:
        print("Operation cancelled")

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    
    # Define subcommands (add, list)
    subparsers = parser.add_subparsers(dest='command')
    
    # Add subcommand: add
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('task', type=str, help='The task description')
    
    # Add subcommand: list
    list_parser = subparsers.add_parser('list', help='List all tasks')
    #Create a group for mutually exclusive flags
    group = list_parser.add_mutually_exclusive_group()
    #Create a flag for "done" and "pending" tasks in case they want to filter these
    group.add_argument('--done', action='store_true', help='Only show completed tasks')
    group.add_argument('--pending', action='store_true', help='Only show pending tasks')

    # Add subcommand: clear
    clear_parser = subparsers.add_parser('clear', help='Clear all tasks with confirmation')

    # Add subcommand: del
    del_parser = subparsers.add_parser('del', help='Delete a task')
    del_parser.add_argument('index', type=int, help='The index of the task to delete')

    # Add subcommand: done
    done_parser = subparsers.add_parser('done', help='Mark a task as done')
    done_parser.add_argument('index', type=int, help='The index of the task to mark as done')

    # Add subcommand: unrdone
    undone_parser = subparsers.add_parser('undone', help='Mark a task as undone')
    undone_parser.add_argument('index', type=int, help='The index of the task to mark as undone')
    
    # Parse the arguments
    args = parser.parse_args()

    # Handle the commands
    if args.command == 'add':
        add_task(args.task)
    elif args.command == 'list':
        list_tasks(args)
    elif args.command == 'del':
        delete_task(args.index)
    elif args.command == 'done':
        mark_done(args.index)
    elif args.command == 'undone':
        mark_undone(args.index)
    elif args.command == 'clear':
        clear_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()