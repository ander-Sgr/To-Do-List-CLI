from datetime import datetime
from enum import Enum


class __Status(Enum):
    PENDING = 1
    IN_POGRESS = 2
    COMPLETED = 3


class Task:

    def __init__(self, title: str, description: str, status: __Status, completed_at) -> None:
        """
        status: can be - pending, in pogress, completed
        """
        self.id = "?"
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.now()
        self.completed_at = completed_at

    def mark_completed(id: int, data) -> None:
        # to do search in data all the tasks with the id
        # and verify de field status if is 1 then is completed
        # else is incompleted

        pass


print(__Status.COMPLETED)
