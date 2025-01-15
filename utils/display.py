from tasks import Task, Storage
from datetime import datetime


class TasksDisplay:

    def __init__(self, storage: Storage):
        self.storage = storage

    def format_date(self, date_str):
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return date.strftime("%Y-%m-%d %H:%M:%S")

    def show_tasks(self):
        tasks = self.storage.load_tasks()
        for task in tasks:
            formatted_date = self.format_date(task["created_at"])
            print(task["title"], task["description"], task["status"], formatted_date)
