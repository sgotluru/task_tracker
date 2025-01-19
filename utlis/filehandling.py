import json
from .config import get_task_file_path

def initialize_json_file():
    path = get_task_file_path()
    if not path:
        return
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    if not path.exists():
        with path.open("w") as file:
            json.dump([], file)
        print(f"Created JSON file at: {path}.")


def read_json_file():
    path = get_task_file_path()
    if not path:
        return []
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file '{path}': {e}")
        return []
    except IOError as e:
        print(f"Error reading file '{path}': {e}")
        return []
    except Exception as e:
        print(f"Unexpected error while reading file '{path}': {e}")
        return []


def write_json_file(path, data):
    path = get_task_file_path()
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
