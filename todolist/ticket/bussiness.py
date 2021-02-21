from typing import List

from core.response import ErrorType, FieldError
from todolist.board.interfaces import IBoardUseCases
from todolist.board.requests import GetBoard


def validate_board_id(board_id: int, boards_uc: IBoardUseCases) -> FieldError:
    if board_id is None:
        return FieldError(
            field="board_id", type=ErrorType.REQUIRED, message="Board ID is required"
        )

    resp = boards_uc.get_board(req=GetBoard(id=board_id))
    if not resp.is_ok:
        return FieldError(
            field="board_id", type=ErrorType.INVALID, message="Board ID not exists"
        )


def validate_title(title: str) -> FieldError:
    if title is None:
        return FieldError(
            field="title", type=ErrorType.REQUIRED, message="Title is required"
        )

    if not (3 <= len(title) <= 128):
        return FieldError(
            field="title",
            type=ErrorType.INVALID,
            message="Title has a invalid length. Try between 3 and 128 characters ",
        )


def validate_description(description: int) -> FieldError:
    if description is not None and len(description) >= 256:
        return FieldError(
            field="description",
            type=ErrorType.INVALID,
            message="Description has a invalid length. Maximum is 256 characteres.",
        )


def validate_labels(labels: List[str]) -> List[FieldError]:
    errors = []

    for i, label in enumerate(labels):
        if label is None or not isinstance(label, str):
            errors.append(
                FieldError(
                    field=f"labels[{i}]",
                    type=ErrorType.INVALID,
                    message="Label must be strings.",
                )
            )

    return errors
