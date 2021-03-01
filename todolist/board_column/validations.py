from typing import List

from core.response import ErrorType, FieldError


def validate_name(name: str) -> FieldError:
    """
    Field 'name':
    - required
    - string
    - min 3 characters
    - max 32 characters
    """
    if not name:
        return FieldError(
            field="name", type=ErrorType.REQUIRED, message="Name is required"
        )

    if not isinstance(name, str):
        return FieldError(
            field="name", type=ErrorType.INVALID, message="Name must be a string"
        )

    if not (3 <= len(name) <= 32):
        return FieldError(
            field="name",
            type=ErrorType.INVALID,
            message="Name has a invalid length. Try between 3 and 128 characters",
        )


def validate_board_id(board_id: int) -> FieldError:
    """
    Field 'board_id'
    - integer
    - required
    """
    if not board_id:
        return FieldError(
            field="board_id", type=ErrorType.INVALID, message="Board ID is required"
        )

    if not isinstance(board_id, int):
        return FieldError(
            field="board_id",
            type=ErrorType.INVALID,
            message="Board ID must be a integer",
        )
