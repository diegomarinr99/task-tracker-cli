import argparse
from task_manager import TaskManager

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
    group.add_argument('--todo', action='store_true', help='Only show pending tasks')
    group.add_argument('--progress', action='store_true', help='Only show tasks in progress')

    # Add subcommand: clear
    clear_parser = subparsers.add_parser('clear', help='Clear all tasks with confirmation')

    # Add subcommand: del
    del_parser = subparsers.add_parser('del', help='Delete a task')
    del_parser.add_argument('id', type=int, help='The id of the task to delete')

    # Add subcommand: done
    done_parser = subparsers.add_parser('done', help='Mark a task as done')
    done_parser.add_argument('id', type=int, help='The id of the task to mark as done')

    # Add subcommand: todo
    todo_parser = subparsers.add_parser('todo', help='Mark a task as todo')
    todo_parser.add_argument('id', type=int, help='The id of the task to mark as undone')

    # Add subcommand: progress
    progress_parser = subparsers.add_parser('progress', help='Mark a task as in progress')
    progress_parser.add_argument('id', type=int, help='The id of the task to mark as in progress')

    # Add subcommand: update
    update_parser = subparsers.add_parser('update', help='Update a tasks description')
    update_parser.add_argument('id', type=int, help='The id of the task to update')
    update_parser.add_argument('description', type=str, help='The id of the task to update')

    
    # Parse the arguments
    args = parser.parse_args()

    manager = TaskManager()

    # Handle the commands
    if args.command == 'add':
        manager.add_task(args.task)
    elif args.command == 'list':
        manager.list_tasks(args)
    elif args.command == 'del':
        manager.delete_task(args.id)
    elif args.command == 'done':
        manager.mark_done(args.id)
    elif args.command == 'todo':
        manager.mark_todo(args.id)
    elif args.command == 'progress':
        manager.mark_progress(args.id)
    elif args.command == 'clear':
        manager.clear_tasks()
    elif args.command == 'update':
        manager.update_task(args.id, args.description)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()