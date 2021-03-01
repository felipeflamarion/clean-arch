from abc import ABC, abstractclassmethod

from core.response import ItemResp, ItemsResp
from todolist.board_column.requests import (
    CreateBoardColumn,
    DeleteBoardColumn,
    GetBoardColumn,
    UpdateBoardColumn,
)
from todolist.entities import BoardColumn


class IBoardColumnRepo(ABC):
    @abstractclassmethod
    def insert_board_column(self, board_column: BoardColumn) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def update_board_column(self, board_column: BoardColumn) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def get_board_column_by_id(self, id: int) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def delete_board_column(self, id: int) -> ItemResp:
        raise NotImplementedError


class IBoardColumnUseCases:
    @abstractclassmethod
    def create_board_column(self, req: CreateBoardColumn) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def update_board_column(self, req: UpdateBoardColumn) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def get_board_column(self, req: GetBoardColumn) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def delete_board_column(self, req: DeleteBoardColumn) -> ItemResp:
        raise NotImplementedError
