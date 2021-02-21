from dataclasses import dataclass
from typing import List


@dataclass
class CreateTicket:
    board_id: int
    title: str
    description: str = None
    labels: List[str] = None


@dataclass
class UpdateTicket:
    id: int
    title: str
    description: str = None
    labels: List[str] = None


@dataclass
class GetTicket:
    id: int


@dataclass
class DeleteTicket:
    id: int
