from tasks import Task, TaskManager, Status
from utils import TasksDisplay

import json

task_manager = TaskManager()

task_manager.add_task(Task("Learn python 1", "Improve skill in python"))
task_manager.add_task(Task("Learn python 2", "Improve skill in python"))
task_manager.add_task(Task("Learn python 3", "Improve skill in python"))


# for task in task_manager.tasks:
#    if task.id == 1:
#       print(task.to_dict())


task = task_manager.get_task(1)
if task:
    print(task.to_dict()["title"])
else:
    print("no existe")

task_manager.edit_task(1, "learn python 23", "", Status.IN_PROGRESS)
task2 = task_manager.get_task(1)
if task:
    print(task.to_dict()["title"])
else:
    print("no existe")


task_manager.delete_task(1)
print([task.to_dict() for task in task_manager.list_tasks()])