from typing import List

from core.response import FieldError, HttpStatus, ItemResp


def make_errors_from_validations_resp(validations: List[FieldError]):
    errors = []

    for resp in validations:
        if resp is None:
            continue

        if isinstance(resp, FieldError):
            errors.append(resp)

        if isinstance(resp, list):
            errors.extend(resp)

    return errors


def handle_validations(
    fields_validations: List[FieldError] = [],
    bussiness_validations: List[FieldError] = [],
) -> ItemResp:
    errors = []

    if fields_validations:
        errors.extend(make_errors_from_validations_resp(fields_validations))

    if not errors and bussiness_validations:
        errors.extend(make_errors_from_validations_resp(bussiness_validations))

    return (
        ItemResp(status=HttpStatus.OK)
        if not errors
        else ItemResp(status=HttpStatus.BAD_REQUEST, errors=errors)
    )
