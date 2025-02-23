from tasks import Task, TaskManager, Status, Storage
from utils import TasksDisplay
from argparse import ArgumentParser, Namespace
import sys

storage = Storage()
task_manager = TaskManager(storage)
display = TasksDisplay(storage)


def parser_args(args: list) -> Namespace:
    parser = ArgumentParser("TO DO list in cli")

    task_details = parser.add_argument_group("Add new task")
    task_details.add_argument(
        "-c", "--create", action="store_true", help="Add a new task"
    )
    task_details.add_argument("--title", type=str, help="Ttile's task")
    task_details.add_argument("--descrip", type=str, help="Description's task")

    task_list = parser.add_argument_group("List all tasks")
    task_list.add_argument("-l", "--list", action="store_true", help="List all tasks")

    task_edit = parser.add_argument_group("Edit a task")
    task_edit.add_argument("-e", "--edit", type=int, help="the id of the task for edit")
    task_edit.add_argument("--newTitle", type=str, help="Title's task")
    task_edit.add_argument("--newDescrip", type=str, help="Description's task")
    task_edit.add_argument(
        "--completed", choices=["Y", "N"], help="Mark as completed (Y / N)"
    )

    parser.add_argument("-d", "--delete", type=int, help="Delete a task by id")

    return parser.parse_args(args)


def add_new_task(title: str, descrip: str) -> None:
    t = task_manager.add_task(Task(title, descrip))
    display.show_task(t)


def list_tasks():
    display.list_tasks()


def edit_task(
    task_id: int, title: str = None, descip: str = None, completed: str = None
):
    task = task_manager.get_task(task_id)
    if not task:
        print(f"Task with {task_id} id not found")
    print(f"=================== BEFORE EDIT ===================")
    updated_task = Task.from_dict(task)
    display.show_task(updated_task)
    if title:
        updated_task.title = title
    if descip:
        updated_task.description = descip
    if completed:
        if completed.upper() == "Y":
            updated_task.mark_completed()
    task_manager.modify_task(updated_task, task_id)
    print(f"=================== AFTER EDIT ===================")
    display.show_task(updated_task)


def delete_task(task_id: int):
    task = task_manager.get_task(task_id)
    if not task:
        print(f"Task with {task_id} id not found")
    task_manager.delete_task(task_id)


def main(args: list):
    parsed_args = parser_args(args)
    if parsed_args.create:
        add_new_task(parsed_args.title, parsed_args.descrip)
    elif parsed_args.list:
        list_tasks()
    elif parsed_args.edit:
        edit_task(
            parsed_args.edit,
            parsed_args.newTitle,
            parsed_args.newDescrip,
            parsed_args.completed,
        )
    elif parsed_args.delete:
        delete_task(parsed_args.delete)


if __name__ == "__main__":
    main(sys.argv[1:])
