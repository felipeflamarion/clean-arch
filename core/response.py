from typing import Any, List


class HttpStatus:
    OK = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409


class ErrorType:
    REQUIRED = "required"
    INVALID = "invalid"
    CONFLICT = "conflict"


class FieldError:
    def __init__(self, field: str, type: str, message: str):
        self.field = field
        self.type = type
        self.message = message

    def to_json(self):
        return {"field": self.field, "type": self.type, "message": self.message}


class Resp:
    def __init__(self, status: int = None, errors: List[FieldError] = None):
        self.status = status
        self.errors = errors

    @property
    def is_ok(self):
        return (
            True
            if self.status == HttpStatus.OK or (self.status is None and not self.errors)
            else False
        )

    def dump_errors(self):
        return {
            "errors": [field_error.to_json() for field_error in self.errors]
            if self.errors
            else []
        }


class ItemResp(Resp):
    def __init__(self, item: Any = None, *args, **kwargs):
        self.item = item
        super().__init__(*args, **kwargs)


class ItemsResp(Resp):
    def __init__(self, items: List[Any] = None, *args, **kwargs):
        self.items = items
        super().__init__(*args, **kwargs)
