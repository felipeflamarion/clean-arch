from dataclasses import dataclass


@dataclass
class CreateBoardColumn:
    board_id: int
    name: str


@dataclass
class UpdateBoardColumn:
    id: int
    board_id: int
    name: str


@dataclass
class GetBoardColumn:
    id: int
    board_id: int


@dataclass
class DeleteBoardColumn:
    id: int
    board_id: int


@dataclass
class GetBoardColumnsByBoardId:
    board_id: int
