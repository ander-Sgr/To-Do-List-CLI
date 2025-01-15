from .models import Task
import json

class Storage:
    __PATH_JSON = "./data/tasks.json"

    def save_tasks(self, tasks: list[Task]):
        with open(self.__PATH_JSON, 'w') as file:
            for task in tasks:
                file.write(json.dumps(task.to_dict(), indent=4))

    def load_tasks(self):
        pass
