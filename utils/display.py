from tasks import Task, Storage
from datetime import datetime


class TasksDisplay:

    def __init__(self, storage: Storage):
        self.storage = storage

    def format_date(self, date_str):
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return date.strftime("%Y-%m-%d %H:%M:%S")

    def get_max_str(self, tasks, field):
        max_len = 0
        for task in tasks:
            current_len = len(task[field])
            if current_len > max_len:
                max_len = current_len
        return max_len

    def __show_header(self, len_title, len_descrip):
        border_top = f"┏{'━' * (len_title + 2)}┯{'━' * len_descrip}┓"
        header = f"┃ {'Title'.ljust(len_title)} ┃ Description "
        border_bottom = f"┡{'━' * (len_title + 2)}╇{'━' * len_descrip}┩"

        print(border_top)
        print(header)
        print(border_bottom)

    def __show_footer(self, len_title, len_desrip):
        footer = f"└{'─' * (len_title + 2)}┴{'─' * len_desrip}┘"
        print(footer)
        
    # to do 
    def __translate_status(self):
        pass

    def show_tasks(self):
        tasks = self.storage.load_tasks()
        max_len_title = self.get_max_str(tasks, "title")
        max_len_descrip = self.get_max_str(tasks, "description")
        self.__show_header(max_len_title, max_len_descrip)
        for task in tasks:
            title = task["title"].ljust(max_len_title)
            description = task.get("description", "").ljust(max_len_descrip - 2)
            status = task.get('status')
            print(f"│ {title} │ {description} | {status}")
        self.__show_footer(max_len_title, max_len_descrip)
        # print(title_max_len)

    """
           ┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━ ┓                                                    
           ┃ Title            ┃ Description           ┃ Status  ┃                                                    
           ┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━╇ ━━━━━━  ╇                                              
           │ Learn python 1   │ Update Ubuntu VM      │  x      │                                                    
           │ About the aws HA │ Setup Nginx In Ubuntu │         |                                               
           └──────────────────┴───────────────────────┴─────── ┘ 
    """
