from core.bases.api import APIBase
from flask import request
from todolist.board.requests import CreateBoard, DeleteBoard, GetBoard, UpdateBoard


class BoardListAPI(APIBase):
    def __init__(self, use_cases, *args, **kwargs):
        self.use_cases = use_cases
        super().__init__(*args, **kwargs)

    def set_methods(self):
        return {"GET": self.get, "POST": self.create}

    def get(self, *args, **kwargs):
        resp = self.use_cases.get_boards()

        return {
            "boards": [item.to_json() for item in resp.items]
            if resp.is_ok
            else resp.dump_errors()
        }, resp.status

    def create(self, *args, **kwargs):
        resp = self.use_cases.create_board(CreateBoard(title=request.json.get("title")))

        return resp.item.to_json() if resp.is_ok else resp.dump_errors(), resp.status


class BoardSingleAPI(APIBase):
    def __init__(self, use_cases, *args, **kwargs):
        self.use_cases = use_cases
        super().__init__(*args, **kwargs)

    def set_methods(self):
        return {"GET": self.get_by_id, "PUT": self.update, "DELETE": self.delete}

    def get_by_id(self, id: int):
        resp = self.use_cases.get_board(req=GetBoard(id=id))

        return resp.item.to_json() if resp.is_ok else resp.dump_errors(), resp.status

    def update(self, id: int):
        resp = self.use_cases.update_board(
            req=UpdateBoard(id=id, title=request.json.get("title"))
        )

        return resp.item.to_json() if resp.is_ok else resp.dump_errors(), resp.status

    def delete(self, id: int):
        resp = self.use_cases.delete_board(req=DeleteBoard(id=id))

        return {} if resp.is_ok else resp.dump_errors(), resp.status


def register_routes(app, use_cases):
    board_list_api = BoardListAPI(use_cases)
    board_single_api = BoardSingleAPI(use_cases)

    board_list_api.register_api(
        app,
        "/api/todolist/boards",
        "todolist.boards.list",
    )
    board_single_api.register_api(
        app,
        "/api/todolist/boards/<int:id>",
        "todolist.boards.single",
    )
