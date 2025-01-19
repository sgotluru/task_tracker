import json
from .config import get_task_file_path
from pathlib import Path

def initialize_json_file():
    path = get_task_file_path()
    if not path:
        print("Task file path not found.")
        return
    
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    if not path.exists():
        with path.open("w", encoding="utf-8") as file:
            json.dump([], file)
        print(f"Created JSON file at: {path}.")


def read_json_file():
    path = get_task_file_path()
    if not path:
        print("Task file path not found.")
        return []
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File '{path}' not found. Initializing with empty list.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file '{path}': {e}. Initializing with empty list.")
        return []
    except IOError as e:
        print(f"Error reading file '{path}': {e}. Initializing with empty list.")
        return []
    except Exception as e:
        print(f"Unexpected error while reading file '{path}': {e}. Initializing with empty list.")
        return []


def write_json_file(path, data):
    path = get_task_file_path()
    if not path:
        print("Task file path is not configured.")
        return

    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Data successfully written to file: {path}.")
    except IOError as e:
        print(f"Error writing to file '{path}': {e}")