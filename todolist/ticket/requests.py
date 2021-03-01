from dataclasses import dataclass
from typing import List


@dataclass
class CreateTicket:
    board_column_id: int
    title: str
    description: str = None
    priority: int = 0
    labels: List[str] = None


@dataclass
class UpdateTicket:
    id: int
    board_column_id: int
    title: str
    description: str = None
    priority: int = 0
    labels: List[str] = None


@dataclass
class GetTicket:
    id: int


@dataclass
class DeleteTicket:
    id: int
