from typing import Any, List


class HttpStatus:
    OK = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409


class Resp:
    def __init__(self, status: int = None, errors: List[dict] = None):
        self.status = status
        # TODO: Melhorar error resp
        self.errors = errors

    @property
    def is_ok(self):
        # TODO: implement
        pass


class ItemResp(Resp):
    def __init__(self, item: Any = None, *args, **kwargs):
        self.item = item
        super().__init__(*args, **kwargs)


class ItemsResp(Resp):
    def __init__(self, items: List[Any] = None, *args, **kwargs):
        self.items = items
        super().__init__(*args, **kwargs)
