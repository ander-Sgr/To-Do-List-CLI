from .models import Task, Status


class TaskManager:
    def __init__(self, tasks: list[Task] = None) -> None:
        self.tasks = tasks if tasks is not None else []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def __exist_task(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None

    def get_task(self, task_id: int):
        task = self.__exist_task(task_id)
        if task:
            return task

    def edit_task(self, task_id: int, title: str, description: str, status: Status):
        task = self.__exist_task(task_id)
        if task:
            task.title = title
            task.description = description
            task.status = status

    def delete_task(self, task_id: int):
        task = self.__exist_task(task_id)
        if task:
            self.tasks.remove(task)
