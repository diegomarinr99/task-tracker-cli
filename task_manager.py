import os
import json
from task import Task

class TaskManager:

    TASKS_FILE = "tasks.json"

    def __init__(self):
        self.tasks = []
        if os.path.exists(self.TASKS_FILE):
            self.load_file()
    
    def load_file(self):
        """Load tasks from the tasks.json file"""
        #Open the file
        with open(self.TASKS_FILE,"r") as file:
            task_data = json.load(file)
            self.tasks = [Task(**task) for task in task_data]

        if self.tasks:
            TaskManager.next_id = max(task.get_id() for task in self.tasks) + 1
        else:
            TaskManager.next_id = 1
    
    def save_file(self):
        """Save current task to the file."""
        if self.tasks:
            task_list = [task.get_dict() for task in self.tasks]
            with open (self.TASKS_FILE, "w") as file:
                json.dump(task_list, file)
        else:
            with open (self.TASKS_FILE, "w") as file:
                json.dump("", file)

    def add_task(self, description):
        """Adds a new task"""
        new_task = Task(self.next_id, description)
        self.tasks.append(new_task)
        TaskManager.next_id += 1
        self.save_file()
        print(f"Task {description} was added succesfully")
    
    def list_tasks(self, args):
        """Lists all tasks that are currently saved"""
        if not self.tasks:
            print("There are no tasks to list")
        else:
            list_tasks = [task.get_dict() for task in self.tasks]
            count = 0
            for task in list_tasks:
                if args.done and (task['status'] == "todo" or task['status'] == 'progress'):
                    continue
                if args.todo and (task['status'] == "done" or task['status'] == 'progress'):
                    continue
                if args.progress and (task['status'] == "todo" or task['status'] == 'done'):
                    continue
                count+=1
                print(f"{task['id']}. [{task['status']}] {task['description']}, created: {task['createdAt']}, last modified: {task['updatedAt']}")
            
            if count == 0:
                if args.done:
                    args_name = "done"
                elif args.progress:
                    args_name = "in-progress"
                elif args.todo:
                    args_name = "todo"
                print(f"There are no tasks with the {args_name} status")
    
    def delete_task(self, id):
        """Deletes a task with an id"""
        if not self.tasks:
            print("There is no tasks to delete.")
        else:
            index = self.find_task(id)
            if index == -1:
                print("The ID does not exist")
            else:
                task = self.tasks[index]
                confirm = input("Are you sure you want to delete this task? This CANNOT be undone (y/n): ")
                if confirm.lower() == 'y':
                    print(f"Deleting task {task.get_description()} with id {id}")
                    del self.tasks[index]
                    print("Task has been deleted successfully")
                    self.save_file()
                else:
                    print("Operation cancelled")
        
    
    def mark_todo(self, id):
        if not self.tasks:
            print("There are no tasks to mark as todo")
        else:
            index = self.find_task(id)
            if index == -1:
                print("There is no task with ID {id}")
            else:
                task = self.tasks[index]
                if task.get_status() == "todo":
                    print("The task is already marked as todo")
                else:
                    task.set_status("todo")
                    self.save_file()
                    print(f"Task {task.get_description()} has been marked as todo.")
    
    def mark_progress(self, id):
        if not self.tasks:
            print("There are no tasks to mark as in progress")
        else:
            index = self.find_task(id)
            if index == -1:
                print("There is no task with ID {id}")
            else:
                task = self.tasks[index]
                if task.get_status() == "progress":
                    print("The task is already marked as in progress")
                else:
                    task.set_status("progress")
                    self.save_file()
                    print(f"Task {task.get_description()} has been marked as in progress.")
    
    def mark_done(self, id):
        if not self.tasks:
            print("There are no tasks to mark as done")
        else:
            index = self.find_task(id)
            if index == -1:
                print(f"There is no task with ID {id}")
            else:
                task = self.tasks[index]
                if task.get_status() == "done":
                    print("The task is already marked as done")
                else:
                    task.set_status("done")
                    print(task.get_status())
                    self.save_file()
                    print(f"Task {task.get_description()} has been marked as done.")
    
    def clear_tasks(self):
        confirm = input("Are you sure you want to delete all tasks? This CANNOT be undone (y/n): ")
        if confirm.lower() == 'y':
            self.tasks.clear()
            self.save_file()
            print("All tasks have been cleared.")
        else:
            print("Operation cancelled")

    def update_task(self, id, description):
        index = self.find_task(id)
        if index == -1:
            print(f"The ID {id} is not assigned to task")
        else:
            task = self.tasks[index]
            task.set_description(description)
            self.save_file()
            print(f"The task with ID {id} has been updated to {description}")

    def find_task(self, id):
        """Finds the index of the task with a given Id, return -1 if the id is not in the list"""
        if id < 1:
            return -1
        for idx, task in enumerate(self.tasks):
            if task.get_id() == id:
                return idx
        return -1
            



        
