from dataclasses import dataclass
from typing import List
from pendulum import DateTime


@dataclass
class Ticket:
    id: int = None
    title: str = None
    description: str = None
    labels: List[str] = None
    creation_date: DateTime = None

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "labels": self.labels,
            "creation_date": self.creation_date,
        }
