from abc import ABC, abstractclassmethod

from core.response import ItemResp, ItemsResp
from todolist.board.requests import CreateBoard, DeleteBoard, GetBoard, UpdateBoard
from todolist.entities import Board


class IBoardRepo(ABC):
    @abstractclassmethod
    def insert_board(self, board: Board) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def update_board(self, board: Board) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def get_boards(self) -> ItemsResp:
        raise NotImplementedError

    @abstractclassmethod
    def get_board_by_id(self, id: int) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def delete_board(self, id: int) -> ItemResp:
        raise NotImplementedError


class IBoardUseCases:
    @abstractclassmethod
    def create_board(self, req: CreateBoard) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def update_board(self, req: UpdateBoard) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def get_board(self, req: GetBoard) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def get_boards(self) -> ItemsResp:
        raise NotImplementedError

    @abstractclassmethod
    def delete_board(self, req: DeleteBoard) -> ItemResp:
        raise NotImplementedError
