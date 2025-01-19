import yaml
from pathlib import Path
from .parser import get_parsed_arguments
from .commands import add, update, delete, list_status
from .filehandling import initialize_json_file
from .config import update_config, read_config
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    try:
        initialize_json_file()
    except Exception as e:
        logging.error(f"An error occurred while initializing the task file: {e}")
        return
        
    try:
        args = get_parsed_arguments()
        command_map = {
            "add": add,
            "update": update,
            "delete": delete,
            "list": list_status,
        }

        if args.command in command_map:
            command_map[args.command](args)

        elif args.command == "mark-in-progress":
            args.status = "in-progress"
            update(args)

        elif args.command == "mark-done":
            args.status = "done"
            update(args)

        elif args.command == "config":
            if args.tasks_file:
                update_config("settings", "task_file", args.tasks_file)
                logging.info(f"Updated tasks file path to: {args.tasks_file}")
            elif args.show:
                config = read_config()
                logging.info("Current Configuration:")
                print(yaml.dump(config, default_flow_style=False))
            else:
                logging.warning("No settings provided to update.")

        else:
            valid_commands = ["add", "update", "delete", "mark-in-progress", "mark-done", "list", "config"]
            logging.error(f"Invalid command. Use one of: {', '.join(valid_commands)}. Use 'tasktkr -h' for help.")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")