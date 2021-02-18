from typing import List

from core.response import FieldError, HttpStatus, ItemResp


def handle_validations(validations_resp: List[FieldError]) -> ItemResp:
    errors = list(filter(lambda resp: resp is not None, validations_resp))

    return (
        ItemResp(status=HttpStatus.OK)
        if not errors
        else ItemResp(status=HttpStatus.BAD_REQUEST, errors=errors)
    )
