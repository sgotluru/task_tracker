from datetime import datetime
from pathlib import Path
from .filehandling import read_json_file, write_json_file

FILE_PATH = "tasks.json"
FILE_PATH = Path.home() / ".taskmanager" / "tasks.json"

def add(args):
    tasks = read_json_file(FILE_PATH)
    title = " ".join(args.title)
    new_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    new_task = {
        "id": new_id,
        "title": title,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    tasks.append(new_task)
    write_json_file(FILE_PATH, tasks)
    print(f"Task '{title}' added successfully with ID: {new_task['id']}")

def update(args):
    tasks = read_json_file(FILE_PATH)
    
    if not args.id:
        print("Task ID is required for updating a task.")
        return
    
    task_id = args.id
    updated = False
    
    for task in tasks:
        if task["id"] == task_id:
            if args.title and args.title != "-":
                task["title"] = task["title"]
                
                valid_statuses = ["todo", "in-progress", "done"]
                if args.status and args.status in valid_statuses:
                    task["status"] = args.status
                elif args.status:
                    print(f"Invalid status: {args.status}. Valid statuses are: {', '.join(valid_statuses)}")
                    return
                
            task["updatedAt"] = datetime.now().isoformat()
            updated = True
            break
        
    if updated:
        write_json_file(FILE_PATH, tasks)
        print(f"Task ID {task_id} updated successfully.")
    else:
        print(f"Task ID {task_id} not found.")

def delete(args):
    tasks = read_json_file(FILE_PATH)
    
    if not args.id:
        print("Task ID is required for deleting a task.")
        return
    
    task_id = args.id
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) < len(tasks):
        write_json_file(FILE_PATH, new_tasks)
        print(f"Task ID {task_id} deleted successfully.")
    else:
        print(f"Task ID {task_id} not found.")

def list_status(args):
    tasks = read_json_file(FILE_PATH)
    valid_statuses = ["todo", "in-progress", "done", "all"]
    
    if args.status not in valid_statuses:
        print(f"Invalid status: {args.status}. Valid statuses are: {', '.join(valid_statuses)}")
        return
    
    if args.status != "all":
        tasks = [task for task in tasks if task["status"] == args.status]
    
    if not tasks:
        print(f"No tasks found with status: {args.status}")
    else:
        for task in tasks:
            print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}")
