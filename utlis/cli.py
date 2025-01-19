from .parser import get_parsed_arguments
from .commands import add, update, delete, list_status
from .filehandling import initialize_json_file
# from pathlib import Path
import os

FILE_PATH = "tasks.json" # Path(__file__).parent / "tasks.json"

def main():
    if not os.path.exists(FILE_PATH):
        initialize_json_file(FILE_PATH)
        
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
        else:
            print("Invalid command. Use --help for usage information.")
    except Exception as e:
        print(f"An error occurred: {e}")
