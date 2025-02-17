from .models import Task, Status
from .storage import Storage


class TaskManager:
    def __init__(self, storage: Storage) -> None:
        self.storage = storage
        self.tasks = self.storage.load_tasks()

    def convert_task_dict(self, task: Task):
        if isinstance(task, dict):
            data = Task.from_dict(task)
            return data

    def __exists_task(self, id) -> Task:
        for task in self.tasks:
            if task["id"] == id:
                return task
        return None

    def add_task(self, task: Task):
        self.tasks.append(task.to_dict())
        self.storage.save_all_tasks(self.tasks) 

    def get_task(self, id):
        return self.__exists_task(id)

    def modify_task(self, updated_task: Task, id):
        task = self.__exists_task(id)
        if task:
            if isinstance(task, dict):
                task = Task.from_dict(task)
                task.title = updated_task.title
                task.description = updated_task.description
                task.status = updated_task.status
                for i, d in enumerate(self.tasks):
                    if d["id"] == task.id:
                        print(task.title)
                        self.tasks[i] = updated_task.to_dict()
                self.storage.save_all_tasks(self.tasks)
                        
                        
    def delete_task(self, task_id: int):
        task = self.__exist_task(task_id)
        if task:
            self.tasks.remove(task)
