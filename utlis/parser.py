import argparse

def get_parsed_arguments():
    """Set up and return argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        description="Simple CLI Task Manager\n\n"
                    "Examples:\n"
                    "tasktkr add \"Buy groceries\"\n"
                    "tasktkr update 1 --title \"Buy milk\"\n"
                    "tasktkr mark-in-progress 1\n"
                    "tasktkr mark-done 1\n"
                    "tasktkr delete 1\n"
                    "tasktkr list\n"
                    "tasktkr list todo\n"
                    "tasktkr list in-progress\n"
                    "tasktkr list done",
        formatter_class=argparse.RawTextHelpFormatter,
        )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("title", nargs="+", help="Title of the new task")

    # Update command
    parser_update = subparsers.add_parser("update", help="Update a task")
    parser_update.add_argument("id", type=int, metavar="ID", help="ID of the task")
    parser_update.add_argument("--title", nargs="+", metavar="TITLE", help="New title for the task")
    parser_update.add_argument(
        "--status",
        choices=["todo", "in-progress", "done"],
        help="New status for the task (todo, in-progress, done)",
        )

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    # List command
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument(
        "status",
        nargs="?",
        default="all",
        choices=["all", "todo", "in-progress", "done"],
        metavar="STATUS",
        help="Filter tasks by status (default: all)\n"
                "all - Show all tasks\n"
                "todo - Show tasks with status 'todo'\n"
                "in-progress - Show tasks with status 'in-progress'\n"
                "done - Show tasks with status 'done'",
    )

    return parser.parse_args()
