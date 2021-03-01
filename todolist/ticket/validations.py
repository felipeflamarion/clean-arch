from typing import List

from core.response import ErrorType, FieldError
from todolist.board.interfaces import IBoardUseCases
from todolist.board.requests import GetBoard


def validate_board_column_id(board_column_id: int) -> FieldError:
    """
    Field 'board_column_id':
    - required
    - int
    """
    if board_column_id is None:
        return FieldError(
            field="board_column_id",
            type=ErrorType.REQUIRED,
            message="Board Column ID is required",
        )

    if not isinstance(board_column_id, int):
        return FieldError(
            field="board_column_id",
            type=ErrorType.INVALID,
            message="Board Column must be a integer",
        )


def validate_title(title: str) -> FieldError:
    """
    Field 'title':
    - required
    - string
    - min 3 characters
    - max 128 characters
    """
    if title is None:
        return FieldError(
            field="title", type=ErrorType.REQUIRED, message="Title is required"
        )

    if not isinstance(title, str):
        return FieldError(
            field="title", type=ErrorType.INVALID, message="Title must be a string"
        )

    if not (3 <= len(title) <= 128):
        return FieldError(
            field="title",
            type=ErrorType.INVALID,
            message="Title has a invalid length. Try between 3 and 128 characters ",
        )


def validate_description(description: int) -> FieldError:
    """
    Field 'description':
    - not required
    - string
    - max 1024 characters
    """
    if description is None:
        return

    if not isinstance(description, str):
        return FieldError(
            field="description",
            type=ErrorType.INVALID,
            message="Description must be a string",
        )

    if len(description) >= 1024:
        return FieldError(
            field="description",
            type=ErrorType.INVALID,
            message="Description has a invalid length. Maximum is 1024 characteres.",
        )


def validate_priority(priority: int) -> FieldError:
    """
    Field: 'priority'
    - not required
    - integer
    - min 0
    - max 99
    """
    if priority is None:
        return

    if not isinstance(priority, int):
        return FieldError(
            field="priority",
            type=ErrorType.INVALID,
            message="Priority must be a integer",
        )

    if not (0 < priority < 99):
        return FieldError(
            field="priority",
            type=ErrorType.INVALID,
            message="Priority must be a number between 0 and 99",
        )


def validate_labels(labels: List[str]) -> List[FieldError]:
    """
    Field 'labels':
    - not required
    - must be a list of strings
    """
    if labels is None:
        return

    if not isinstance(labels, list):
        return FieldError(
            field="labels",
            type=ErrorType.INVALID,
            message="Labels field must be a list of strings",
        )

    errors = []
    for i, label in enumerate(labels):
        if label is None or not isinstance(label, str):
            errors.append(
                FieldError(
                    field=f"labels[{i}]",
                    type=ErrorType.INVALID,
                    message="Label must be a string",
                )
            )

    return errors
