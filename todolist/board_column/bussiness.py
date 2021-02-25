from todolist.board.interfaces import IBoardUseCases
from todolist.board.requests import GetBoard
from core.response import ErrorType, FieldError


def validate_board_existence(board_id: int, boards_uc: IBoardUseCases):
    resp = boards_uc.get_board(req=GetBoard(id=board_id))
    if resp.is_ok is False:
        return FieldError(
            field="board_id", type=ErrorType.INVALID, message="Inexistent board ID"
        )
