from .models import Task
import json


class Storage:
    __PATH_JSON = "./data/tasks.json"

    def load_tasks(self):
        try:
            with open(self.__PATH_JSON, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_all_tasks(self, tasks: list):
        """Sobrescribe el archivo JSON con todas las tareas actualizadas."""
        try:
            with open(self.__PATH_JSON, "w") as file:
                json.dump(tasks, file, indent=4)
        except Exception as e:
            print(f"Error while saving tasks: {e}")

    # to do
    def backup_data(self):
        pass
