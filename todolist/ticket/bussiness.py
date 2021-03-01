from typing import List

from core.response import ErrorType, FieldError
from todolist.board_column.interfaces import IBoardColumnUseCases
from todolist.board_column.requests import GetBoardColumn


def validate_board_column_id(
    board_column_id: int, board_columns_uc: IBoardColumnUseCases
) -> FieldError:
    """
    Field: 'board_column_id'
    - must be a existent board column ID
    """
    resp = board_columns_uc.get_board_column(req=GetBoardColumn(id=board_column_id))
    if not resp.is_ok:
        return FieldError(
            field="board_column_id",
            type=ErrorType.INVALID,
            message="Board Column ID not exists",
        )
