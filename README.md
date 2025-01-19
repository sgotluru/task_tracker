# Task Manager CLI

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.6+](https://img.shields.io/badge/Python-3.6%2B-blue)

A simple and intuitive command-line task manager to manage your to-dos effectively.

## Features
- Add tasks with a title.
- Update tasks (change title or status).
- Delete tasks by ID.
- List tasks filtered by status (`todo`, `in-progress`, `done`, or `all`).

## Requirements
- Python 3.6 or higher.
- `pip` (Python package manager) installed.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sgotluru/task_tracker.git
   cd task_tracker
   ```
2. Install the package
    ```bash
    pip install .
    ```
    This will install `tasktkr` command globally in your environment.

## Usage
After installation, you can use the `tasktkr` command to manage your tasks.

### Command-line Options
To see all available commands and usage instructions, run:
```bash
tasktkr -h
```
### Examples
#### Help Command
To see all available commands and options, run:
```bash
tasktkr -h
```

#### Add a New Task
To add a task with the title `Buy groceries`:
```bash
tasktkr add "Buy groceries"
```

#### List Tasks
To view tasks filtered by status:
```bash
tasktkr list --status todo  # List tasks with the status "todo"
tasktkr list --status all   # List all tasks
```

#### Update a Task
To update a task's title or status by ID:
```bash
tasktkr update 1 --title "Buy fresh groceries"
tasktkr update 1 --status done
```

#### Delete a Task
To delete a task by ID:
```bash
tasktkr delete 1
```

## File Storage
By default, tasks are stored in a file located in the same directory. The file path is platform-specific:

- **Linux/Mac**: `~/.taskmanager/tasks.json`
- **Windows**: `C:\Users\<username>\.taskmanager\tasks.json`

### Why This Location?
Storing tasks in the user's home directory ensures:
1. **User Data Separation**: Tasks are saved outside the project directory, preventing accidental deletion or modification when managing project files.
2. **Cross-Platform Compatibility**: The location adapts dynamically to the operating system, ensuring consistent behavior for all users.
3. **Hidden Configuration**: On Linux/Mac, the `.taskmanager` directory is hidden, keeping user-specific data unobtrusive.

If you'd like to reset or back up your tasks, you can manually manage the `tasks.json` file in the locations listed above.



## Development
If you want to modify or contribute to the project:
1. Clone the repository as described above.
2. Install the package in development mode:
    ```bash
    pip install -e .
    ```
3. Run the CLI using:
    ```bash
    python -m utils.cli
    ```
## Contributing 
Contributors are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` file for details.
