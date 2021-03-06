from dataclasses import dataclass
from typing import List

from pendulum import DateTime


@dataclass
class Board:
    id: int = None
    title: str = None
    created_at: DateTime = None
    updated_at: DateTime = None

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


@dataclass
class BoardColumn:
    id: int = None
    board_id: int = None
    name: str = None
    created_at: DateTime = None
    updated_at: DateTime = None

    def to_json(self):
        return {
            "id": self.id,
            "board_id": self.board_id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


@dataclass
class Ticket:
    id: int = None
    board_column_id: int = None
    title: str = None
    description: str = None
    priority: int = None
    labels: List[str] = None
    created_at: DateTime = None
    updated_at: DateTime = None

    def to_json(self):
        return {
            "id": self.id,
            "board_column_id": self.board_column_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "labels": self.labels,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
