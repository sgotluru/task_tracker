# Task Manager CLI

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.12+](https://img.shields.io/badge/Python-3.12%2B-blue)
<!-- ![Build Status](https://img.shields.io/github/actions/workflow/status/sgotluru/task_tracker/ci.yml?branch=main) -->
![GitHub Stars](https://img.shields.io/github/stars/sgotluru/task_tracker?style=social)

A simple and intuitive command-line task manager to manage your to-dos effectively.

## Features
- Add tasks with a title.
- Update tasks (change title or status).
- Delete tasks by ID.
- List tasks filtered by status (`todo`, `in-progress`, `done`, or `all`).

## Requirements
- Python 3.12 or higher.
- `pip` (Python package manager) installed.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sgotluru/task_tracker.git
   cd task_tracker
   ```
2. Install runtime dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Install the package
    ```bash
    pip install .
    ```
    This will install `tasktkr` command globally in your environment.

## Usage
After installation, you can use the `tasktkr` command to manage your tasks.

### Examples :
#### Help Command
To see all available commands and options, run:
```bash
tasktkr -h
```

#### Add a New Task
To add a task with the title `Buy groceries`:
```bash
tasktkr add "Buy groceries"
Data successfully written to file: ~/.taskmanager/tasks.yaml.
Task 'Talk to your best-friend' added successfully with ID: 5
```

#### List Tasks
To view tasks filtered by status:
```bash
tasktkr list --status todo  # List tasks with the status "todo"
ID: 1, Title: Buy groceries, Status: todo, Created: 1947-08-15 00:00:00, Updated: 1947-08-15 00:00:00
tasktkr list --status all   # List all tasks
ID: 1, Title: Buy groceries, Status: todo, Created: 1947-08-15 00:00:00, Updated: 1947-08-15 00:00:00
```


#### Update a Task
To update a task's title or status by ID:
```bash
tasktkr update 1 --title "Buy fresh groceries"
Data successfully written to file: ~/.taskmanager/tasks.yaml.
Task ID 1 updated successfully.
tasktkr update 1 --status done
Data successfully written to file: ~/.taskmanager/tasks.yaml.
Task ID 1 updated successfully.
```

#### Delete a Task
To delete a task by ID:
```bash
tasktkr delete 1
Data successfully written to file: ~/.taskmanager/tasks.yaml.
Task ID 1 deleted successfully.
```

## File Storage
By default, tasks are stored in the user's home directory:

- **Linux/Mac**: `~/.taskmanager/tasks.json`
- **Windows**: `C:\Users\<username>\.taskmanager\tasks.json`

Additionally, the `config.yaml` file is created at:

- **Linux/Mac**: `~/.taskmanager/config.yaml`
- **Windows**: `C:\Users\<username>\.taskmanager\config.yaml`

This file stores the path to `tasks.json` and other configuration settings. If you'd like to reset or back up your tasks, you can manually manage these files.


### Why This Location?
Storing tasks in the user's home directory ensures:
1. **User Data Separation**: Tasks are saved outside the project directory, preventing accidental deletion or modification when managing project files.
2. **Cross-Platform Compatibility**: The location adapts dynamically to the operating system, ensuring consistent behavior for all users.
3. **Hidden Configuration**: On Linux/Mac, the `.taskmanager` directory is hidden, keeping user-specific data unobtrusive.

If you'd like to reset or back up your tasks, you can manually manage the `tasks.json` file in the locations listed above.



## Development
If you want to modify or contribute to the project:
1. Clone the repository as described above.
2. Install development dependencies:
    ```bash
    pip install -r requirements-dev.txt
    ```
3. Install the package in development mode:
    ```bash
    pip install -e .
    ```
4. Run the CLI using:
    ```bash
    python -m utils.cli
    ```
## Contributing
Contributors are welcome! Please fork the repository, create a feature branch, and submit a pull request.

To ensure quality, run tests using:
```bash
pytest
```

## License
This project is licensed under the MIT License. See `LICENSE` file for details.
