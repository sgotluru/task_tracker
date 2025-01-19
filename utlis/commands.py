from datetime import datetime
from .filehandling import read_json_file, write_json_file

def add(args):
    tasks = read_json_file()
    title = " ".join(args.title)
    new_id = max((task["id"] for task in tasks), default = 0) + 1 
    new_task = {
        "id": new_id,
        "title": title,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    tasks.append(new_task)
    write_json_file(tasks)
    print(f"Task '{title}' added successfully with ID: {new_task['id']}")

def update(args):
    tasks = read_json_file()
    task_id = args.id
  
    for task in tasks:
        if task["id"] == task_id:
            
            if args.title:
                task["title"] = " ".join(args.title)
            
            if args.status:
                task["status"] = args.status
            task["updatedAt"] = datetime.now().isoformat()
            write_json_file(tasks)
            print(f"Task ID {task_id} updated successfully.")
            return         
    
    print(f"Task ID {task_id} not found.")

def delete(args):
    tasks = read_json_file()
    task_id = args.id
    
    new_tasks = [task for task in tasks if task["id"] != task_id]
    
    if len(new_tasks) < len(tasks):
        write_json_file(new_tasks)
        print(f"Task ID {task_id} deleted successfully.")
    else:
        print(f"Task ID {task_id} not found.")

def list_status(args):
    tasks = read_json_file()
    
    if args.status != "all":
        filtered_tasks = [task for task in tasks if task["status"] == args.status]
    else:
        filtered_tasks = tasks

    # Check if there are any tasks to display
    if not filtered_tasks:
        print(f"No tasks found with status: {args.status}")
        return

    # Display each task with formatted timestamps
    for task in filtered_tasks:
        created_at = datetime.fromisoformat(task["createdAt"]).strftime("%Y-%m-%d %H:%M:%S")
        updated_at = datetime.fromisoformat(task["updatedAt"]).strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}, "
            f"Created: {created_at}, Updated: {updated_at}"
        )