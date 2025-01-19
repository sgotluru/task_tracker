from .parser import get_parsed_arguments
from .commands import add, update, delete, list_status
from .filehandling import initialize_json_file
from .config import update_config, read_config
import yaml

import os

def main():
    if not os.path.exists():
        initialize_json_file()
        
    try:
        args = get_parsed_arguments()
        if args.command == "add":
            add(args)
        elif args.command == "update":
            update(args)
        elif args.command == "delete":
            delete(args)
        elif args.command == "mark-in-progress":
            update(args, "in-progress")
        elif args.command == "mark-done":
            update(args, "done")
        elif args.command == "list":
            list_status(args)
        elif args.command == "config":
            if args.tasks_file:
                update_config("settings", "task_file", args.tasks_file)
                print(f"Updated tasks file path to: {args.tasks_file}")
            elif args.show:
                config = read_config()
                print(yaml.dump(config, default_flow_style=False))
            else:
                print("No settings provided to update.")
        else:
            valid_commands = ["add", "update", "delete", "mark-in-progress", "mark-done", "list"]
            print(f"Invalid command. Use one of: {', '.join(valid_commands)}. Use 'tasktkr -h' for help.")
            
    except Exception as e:
        print(f"An error occurred: {e}")
