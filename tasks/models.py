from datetime import datetime
from enum import Enum
from .storage import Storage


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
        id: int = None,
        status: Status = Status.PENDING,
        completed_at: datetime = None,
        created_at: datetime = datetime.now()
    ) -> None:
        self.valid_status(status)
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at
        self.completed_at = completed_at
        self.id = self.set_id(id)

    def mark_completed(self) -> None:
        self.status = Status.COMPLETED
        self.completed_at = datetime.now()

    def set_id(self, id):
        if id is None:
            Task.__current_id += 1
            id = Task.__current_id
        return id

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

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            status=Status(data["status"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            completed_at=(
                datetime.fromisoformat(data["completed_at"])
                if data["completed_at"]
                else None
            ),
        )
