from datetime import datetime
from enum import Enum

from json import dumps


class Status(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In progress"
    COMPLETED = "Completed"


class Task:

    __current_id = 0

    def __init__(
        self,
        title: str,
        description: str,
        status: Status = Status.PENDING,
        completed_at: datetime = None,
    ) -> None:
        self.valid_status(status)
        Task.__current_id += 1
        self.id = Task.__current_id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.now()
        self.completed_at = completed_at

    def mark_completed(self) -> None:
        self.status = Status.COMPLETED
        self.completed_at = datetime.now()

    @classmethod
    def reset_id(cls):
        cls.__current_id = 0

    @classmethod
    def valid_status(self, status):
        if not isinstance(status, Status):
            raise ValueError(f"Invalid Status: {status}")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "completed_at": (
                self.completed_at.isoformat() if self.completed_at else None
            ),
        }


task = Task("Learn Python", "Improve python skill")

task_dict = task.to_dict()

task_json = dumps(task_dict, indent=4)

print(task_json)
