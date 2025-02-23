from tasks import Task, TaskManager, Status, Storage
from utils import TasksDisplay
from argparse import ArgumentParser, Namespace
import sys

storage = Storage()

display = TasksDisplay(storage)


def parser_args(args: list) -> Namespace:
    parser = ArgumentParser("TO DO list in cli")
    
    required = parser.add_argument_group('required arguemnts')
    required.add_argument('-c', '--create', action='store_true',
                          help="Add a new task")
    task_details = parser.add_argument_group('task details')
    task_details.add_argument('--title', type=str, help="Ttile's task")
    task_details.add_argument('--descrip', type=str, help="Description's task")
    
    return parser.parse_args(args)
    

def add_new_task(title: str, descrip: str) -> None:
    task_manager = TaskManager(storage)
    task_manager.add_task(Task(title, descrip))
    # display.show_task(task.id)
    

def main(args: list):
    parsed_args = parser_args(args)
    if parsed_args.create:
       add_new_task(parsed_args.title, parsed_args.descrip)
    
if __name__ == "__main__":
    main(sys.argv[1:])