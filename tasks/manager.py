from .models import Task, Status
from .storage import Storage


class TaskManager:
    def __init__(self, storage: Storage) -> None:
        self.storage = storage
        self.tasks = self.storage.load_tasks()
        self.last_id = self.get_last_id()

    def convert_task_dict(self, task: Task):
        if isinstance(task, dict):
            data = Task.from_dict(task)
            return data

    def get_last_id(self):
        if self.tasks:
            return max(task["id"] for task in self.tasks)
        return 0

    def __exists_task(self, id) -> Task:
        for task in self.tasks:
            if task["id"] == id:
                return task
        return None

    def add_task(self, task: Task):
        self.last_id += 1
        task.id = self.last_id
        self.tasks.append(task.to_dict())
        self.storage.save_all_tasks(self.tasks)
        return task

    def get_task(self, id):
        return self.__exists_task(id)

    def modify_task(self, updated_task: Task, id):
        task = self.__exists_task(id)
        if task:
            if isinstance(task, dict):
                task = Task.from_dict(task)
                for i, t in enumerate(self.tasks):
                    if t["id"] == task.id:
                        self.tasks[i] = updated_task.to_dict()
                self.storage.save_all_tasks(self.tasks)
        return task

    def delete_task(self, task_id: int):
        task = self.__exists_task(task_id)
        if task:
            self.tasks = [t for t in self.tasks if t["id"] != task_id]
            self.storage.save_all_tasks(self.tasks)
