from tasks import Task, TaskManager, Status, Storage
from utils import TasksDisplay

storage = Storage()
task_manager = TaskManager(storage)
display = TasksDisplay(storage)

#task_manager.add_task(Task("Nuevo item", "realizar un insert"))
#task_manager.add_task(Task("Nuevo item", "realizar un insert"))
#task_manager.add_task(Task("Nuevo item", "realizar un insert"))
#task_manager.add_task(Task("Nuevo item", "realizar un insert"))
t = task_manager.get_task(2)
new_task = (Task("hola", "descip", t['id']))
task_new = task_manager.modify_task(new_task, t['id'])
print("----------------")
print(t)
display.show_tasks()
