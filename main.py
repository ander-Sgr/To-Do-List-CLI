from tasks import Task, TaskManager, Status, Storage
from utils import TasksDisplay
from datetime import datetime

task_manager = TaskManager()
storage = Storage()
display = TasksDisplay(storage)


task_manager.add_task(Task("Learn python 1", "Improve skill in python"))
task_manager.add_task(Task("Learn python 2", "Improve skill in python"))
task_manager.add_task(
    Task(
        "Learn about Pulimi with python",
        "I have to see some tutorials about how can in implement it",
    )
)


storage.save_tasks(task_manager.tasks)
task_manager.edit_task(task_id=task_manager.get_task(1), completed_at=datetime.now())
display.show_tasks()
