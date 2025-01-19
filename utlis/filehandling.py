import json

def initialize_json_file(path, initial_data=None):
    if initial_data is None:
        initial_data = []
    try:
        with open(path, 'w') as file:
            json.dump(initial_data, file, indent=4)
        print(f"Created file '{path}' with initial data: {initial_data}")
    except IOError as e:
        print(f"Failed to create file '{path}': {e}")
    except Exception as e:
        print(f"Unexpected error creating file '{path}': {e}")


def read_json_file(path):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
        print(f"Data read successfully from '{path}'.")
        return data
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"File '{path}' is not valid JSON.")
        return None
    except IOError as e:
        print(f"Error reading file '{path}': {e}")
        return None
    except Exception as e:
        print(f"Unexpected error while reading the file '{path}': {e}")
        return None


def write_json_file(path, data):
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data written successfully to '{path}'.")
    except IOError as e:
        print(f"Error writing to file '{path}': {e}")
    except Exception as e:
        print(f"Unexpected error while writing file '{path}': {e}")
