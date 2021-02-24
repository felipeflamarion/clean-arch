from typing import List

from core.response import ErrorType, FieldError


def validate_title(title: str) -> FieldError:
    """
    Field 'title':
    - required
    - min 3 characters
    - max 128 characters
    """
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
