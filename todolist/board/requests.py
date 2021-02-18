from dataclasses import dataclass


@dataclass
class CreateBoard:
    title: str


@dataclass
class UpdateBoard:
    id: int
    title: str


@dataclass
class GetBoard:
    id: int


@dataclass
class DeleteBoard:
    id: int