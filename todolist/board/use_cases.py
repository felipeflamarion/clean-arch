import pendulum as datetime
from core.response import HttpStatus, ItemResp
from todolist.board.interfaces import IBoardRepo, IBoardUseCases
from todolist.board.requests import CreateBoard, DeleteBoard, GetBoard, UpdateBoard
from todolist.entities import Board


class BoardUseCases(IBoardUseCases):
    def __init__(self, repo: IBoardRepo):
        self.repo = repo

    def create_board(self, req: CreateBoard):
        board = Board(
            title=req.title,
            creation_date=datetime.now(),
        )
        return self.repo.insert_board(board)

    def update_board(self, req: UpdateBoard):
        resp = self.repo.get_board_by_id(id=req.id)
        if not resp.item:
            return resp

        board = Board(
            id=req.id,
            title=req.title,
            creation_date=resp.item.creation_date,
        )
        return self.repo.update_board(board)

    def get_board(self, req: GetBoard):
        return self.repo.get_board_by_id(id=req.id)

    def get_boards(self):
        return self.repo.get_boards()

    def delete_board(self, req: DeleteBoard):
        return self.repo.delete_board(id=req.id)
