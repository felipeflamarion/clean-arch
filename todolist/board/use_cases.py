import pendulum as datetime
from core.response import HttpStatus, ItemResp
from core.validations import handle_validations
from todolist.board import validations
from todolist.board.interfaces import IBoardRepo, IBoardUseCases
from todolist.board.requests import CreateBoard, DeleteBoard, GetBoard, UpdateBoard
from todolist.entities import Board


class BoardUseCases(IBoardUseCases):
    def __init__(self, repo: IBoardRepo):
        self.repo = repo

    def create_board(self, req: CreateBoard):
        resp = handle_validations(
            fields_validations=[validations.validate_title(req.title)]
        )
        if not resp.is_ok:
            return resp

        created_at = datetime.now()

        board = Board(
            title=req.title,
            created_at=created_at,
            updated_at=created_at,
        )
        return self.repo.insert_board(board)

    def update_board(self, req: UpdateBoard):
        resp = self.repo.get_board_by_id(id=req.id)
        if not resp.item:
            return resp
        board = resp.item

        resp = handle_validations(
            fields_validations=[validations.validate_title(req.title)]
        )
        if not resp.is_ok:
            return resp

        updated_at = datetime.now()

        board = Board(
            id=req.id,
            title=req.title,
            created_at=board.created_at,
            updated_at=updated_at,
        )
        return self.repo.update_board(board)

    def get_board(self, req: GetBoard):
        return self.repo.get_board_by_id(id=req.id)

    def get_boards(self):
        return self.repo.get_boards()

    def delete_board(self, req: DeleteBoard):
        return self.repo.delete_board(id=req.id)
