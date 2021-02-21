from typing import List

from core.response import FieldError, HttpStatus, ItemResp


def handle_validations(validations_resp: List[FieldError]) -> ItemResp:
    errors = []

    for resp in validations_resp:
        if resp is None:
            continue

        if isinstance(resp, FieldError):
            errors.append(resp)

        if isinstance(resp, list):
            errors.extend(resp)

    return (
        ItemResp(status=HttpStatus.OK)
        if not errors
        else ItemResp(status=HttpStatus.BAD_REQUEST, errors=errors)
    )
