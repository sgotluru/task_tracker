from datetime import datetime
from .filehandling import read_json_file, write_json_file

FILE_PATH = "tasks.json"

def add(args):
    tasks = read_json_file(FILE_PATH)
    title = " ".join(args.title)
    new_task = {
        "id": len(tasks) + 1,
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
    task_id = args.id
    updated = False
    
    for task in tasks:
        if task["id"] == task_id:
            if args.title == "-":
                task["title"] = task["title"]
            elif args.title:
                task["title"] = " ".join(args.title)
                
            if args.status:
                task["status"] = args.status
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
    task_id = args.id
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) < len(tasks):
        write_json_file(FILE_PATH, new_tasks)
        print(f"Task ID {task_id} deleted successfully.")
    else:
        print(f"Task ID {task_id} not found.")

def list_status(args):
    tasks = read_json_file(FILE_PATH)
    if args.status == "in-progress":
        tasks = [task for task in tasks if task["status"] == "in-progress"]
    elif args.status == "done":
        tasks = [task for task in tasks if task["status"] == "done"]
    elif args.status == "todo":
        tasks = [task for task in tasks if task["status"] == "todo"]
    elif args.status == "all":
        tasks = [task for task in tasks]
    else:
        print(f"Invalid status: {args.status}")
        return
    
    if not tasks:
        print(f"No tasks found with status: {args.status}")
    else:
        for task in tasks:
            print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}")
