from .models import Task
import json


class Storage:
    __PATH_JSON = "./data/tasks.json"

    def save_tasks(self, tasks: list[Task]):
        with open(self.__PATH_JSON, "w") as file:
            data = []
            for task in tasks:
                data.append(task.to_dict())
            json.dump(data, file, indent=4)

    def load_tasks(self):
        with open(self.__PATH_JSON, "r") as file:
            data = json.load(file)
            return data

    # to do
    def backup_data(self):
        pass
