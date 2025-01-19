import argparse

def get_parsed_arguments():
    """Set up and return argument parser for the CLI."""
    parser = argparse.ArgumentParser(description="Simple CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("title", nargs="+", help="Title of the new task")

    # Update command
    parser_update = subparsers.add_parser("update", help="Update a task")
    parser_update.add_argument("id", type=int, help="ID of the task")
    parser_update.add_argument("--title", nargs="+", help="New title")
    parser_update.add_argument("--status", choices=["todo", "in-progress", "done"], help="New status")

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task")

    # List command
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument(
        "status",
        nargs="?",
        default="all",
        choices=["all", "todo", "in-progress", "done"],
        help="Filter tasks by status",
    )

    return parser.parse_args()
