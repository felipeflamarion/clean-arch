import pendulum as datetime
from core.response import HttpStatus, ItemResp
from core.validations import handle_validations
from todolist.board.interfaces import IBoardUseCases
from todolist.board_column import bussiness, validations
from todolist.board_column.interfaces import IBoardColumnRepo, IBoardColumnUseCases
from todolist.board_column.requests import (
    CreateBoardColumn,
    DeleteBoardColumn,
    GetBoardColumn,
    GetBoardColumnsByBoardId,
    UpdateBoardColumn,
)
from todolist.entities import BoardColumn


class BoardColumnUseCases(IBoardColumnUseCases):
    def __init__(self, repo: IBoardColumnRepo, boards_uc: IBoardUseCases):
        self.repo = repo
        self.boards_uc = boards_uc

    def create_board_column(self, req: CreateBoardColumn):
        resp = handle_validations(
            fields_validations=[
                validations.validate_board_id(req.board_id),
                validations.validate_name(req.name),
            ],
            bussiness_validations=[
                bussiness.validate_board_existence(req.board_id, self.boards_uc)
            ],
        )
        if not resp.is_ok:
            return resp

        created_at = datetime.now()

        board_column = BoardColumn(
            board_id=req.board_id,
            name=req.name,
            created_at=created_at,
            updated_at=created_at,
        )
        return self.repo.insert_board_column(board_column)

    def update_board_column(self, req: UpdateBoardColumn):
        if bussiness.validate_board_existence(req.board_id, self.boards_uc):
            return ItemResp(status=HttpStatus.NOT_FOUND)

        resp = self.repo.get_board_column_by_id(id=req.id)
        if not resp.item:
            return resp
        board_column = resp.item

        resp = handle_validations(
            fields_validations=[validations.validate_name(req.name)],
        )
        if not resp.is_ok:
            return resp

        updated_at = datetime.now()

        board_column = BoardColumn(
            id=req.id,
            board_id=board_column.board_id,
            name=req.name,
            created_at=board_column.created_at,
            updated_at=updated_at,
        )
        return self.repo.update_board_column(board_column)

    def get_board_column(self, req: GetBoardColumn):
        if bussiness.validate_board_existence(req.board_id, self.boards_uc):
            return ItemResp(status=HttpStatus.NOT_FOUND)

        return self.repo.get_board_column_by_id(id=req.id)

    def get_board_columns_by_board_id(self, req: GetBoardColumnsByBoardId):
        if bussiness.validate_board_existence(req.board_id, self.boards_uc):
            return ItemResp(status=HttpStatus.NOT_FOUND)

        return self.repo.get_board_columns_by_board_id(board_id=req.board_id)

    def delete_board_column(self, req: DeleteBoardColumn):
        if bussiness.validate_board_existence(req.board_id, self.boards_uc):
            return ItemResp(status=HttpStatus.NOT_FOUND)

        return self.repo.delete_board_column(id=req.id)
