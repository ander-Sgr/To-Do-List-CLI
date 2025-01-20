from tasks import Task, Storage
from datetime import datetime


class TasksDisplay:

    def __init__(self, storage: Storage):
        self.storage = storage

    def __format_date(self, date_str):
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return date.strftime("%Y-%m-%d %H:%M:%S")

    def __get_max_str(self, tasks, field):
        max_len = 0
        for task in tasks:
            if task[field] is None:
                current_len = 0
            else:
                current_len = len(task[field])

            if current_len > max_len:
                max_len = current_len
        return max_len

    def __show_header(
        self, len_title, len_descrip, len_status, len_created_at, len_completed_at
    ):
        border_top = f"┌{'─' * (len_title + 2)}┬{'─' * (len_descrip + 2)}┬{'─' * (len_status + 2)}┬{'─' * (len_created_at + 2)}┬{'─' * (len_completed_at + 2)}┐"
        header = f"│ {'Title'.center(len_title)} │ {'Description'.center(len_descrip)} │ {'Status'.center(len_status)} │ {'Created at'.center(len_created_at)} │ {'Completed at'.center(len_completed_at)} │"
        border_bottom = f"├{'─' * (len_title + 2)}┼{'─' * (len_descrip + 2)}┼{'─' * (len_status + 2)}┼{'─' * (len_created_at + 2)}┼{'─' * (len_completed_at + 2)}┤"

        print(border_top)
        print(header)
        print(border_bottom)

    def __show_footer(
        self, len_title, len_descrip, len_status, len_created_at, len_completed_at
    ):
        footer = f"└{'─' * (len_title + 2)}┴{'─' * (len_descrip + 2)}┴{'─' * (len_status + 2)}┴{'─' * (len_created_at + 2)}┴{'─' * (len_completed_at + 2)}┘"
        print(footer)

    def __translate_status(self, status):
        status_map = {
            "completed": "✔ Completed",
            "in_progress": "⏳ In Progress",
            "pending": "🔄 Pending",
        }
        return status_map.get(status)


    def show_tasks(self):
        tasks = self.storage.load_tasks()

        for task in tasks:
            task["created_at"] = self.__format_date(task["created_at"])
            if task["completed_at"]:
                task["completed_at"] = self.__format_date(task["completed_at"])

        max_len_title = self.__get_max_str(tasks, "title")
        max_len_descrip = self.__get_max_str(tasks, "description")
        max_len_status = self.__get_max_str(tasks, "status")
        max_len_created_at = self.__get_max_str(tasks, "created_at")
        max_len_completed_at = max(self.__get_max_str(tasks, "completed_at"), len("N/A"))
        self.__show_header(
            max_len_title,
            max_len_descrip,
            max_len_status,
            max_len_created_at,
            max_len_completed_at,
        )

        for task in tasks:
            title = task["title"].ljust(max_len_title)
            description = task.get("description", "").ljust(max_len_descrip)
            status = task["status"].ljust(max_len_status)
            created_at = task["created_at"].ljust(max_len_created_at)
            completed_at = (
                task["completed_at"].ljust(max_len_completed_at)
                if task["completed_at"]
                else "N/A".ljust(max_len_completed_at)
            )
            print(
                f"│ {title} │ {description} │ {status.center(max_len_status)} │ {created_at} │ {completed_at} │"
            )

        self.__show_footer(
            max_len_title,
            max_len_descrip,
            max_len_status,
            max_len_created_at,
            max_len_completed_at,
        )
