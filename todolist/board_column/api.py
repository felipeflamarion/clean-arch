from core.bases.api import APIBase
from flask import request
from todolist.board_column.requests import (
    CreateBoardColumn,
    DeleteBoardColumn,
    GetBoardColumn,
    UpdateBoardColumn,
)


class BoardColumnListAPI(APIBase):
    def __init__(self, use_cases, *args, **kwargs):
        self.use_cases = use_cases
        super().__init__(*args, **kwargs)

    def set_methods(self):
        return {"POST": self.create}

    def create(self, board_id: int, *args, **kwargs):
        resp = self.use_cases.create_board_column(
            CreateBoardColumn(
                board_id=request.json.get("board_id"), name=request.json.get("name")
            )
        )

        return resp.item.to_json() if resp.is_ok else resp.dump_errors(), resp.status


class BoardColumnSingleAPI(APIBase):
    def __init__(self, use_cases, *args, **kwargs):
        self.use_cases = use_cases
        super().__init__(*args, **kwargs)

    def set_methods(self):
        return {"GET": self.get_by_id, "PUT": self.update, "DELETE": self.delete}

    def get_by_id(self, board_id: int, id: int, *args, **kwargs):
        resp = self.use_cases.get_board_column(
            req=GetBoardColumn(board_id=board_id, id=id)
        )

        return resp.item.to_json() if resp.is_ok else resp.dump_errors(), resp.status

    def update(self, board_id: int, id: int, *args, **kwargs):
        resp = self.use_cases.update_board_column(
            req=UpdateBoardColumn(
                id=id,
                board_id=request.json.get("board_id"),
                name=request.json.get("name"),
            )
        )

        return resp.item.to_json() if resp.is_ok else resp.dump_errors(), resp.status

    def delete(self, id: int, *args, **kwargs):
        resp = self.use_cases.delete_board_column(req=DeleteBoardColumn(id=id))

        return {} if resp.is_ok else resp.dump_errors(), resp.status


def register_routes(app, use_cases):
    board_column_list_api = BoardColumnListAPI(use_cases)
    board_column_single_api = BoardColumnSingleAPI(use_cases)

    board_column_list_api.register_api(
        app,
        "/api/todolist/boards/columns",
        "todolist.board_column.list",
    )
    board_column_single_api.register_api(
        app,
        "/api/todolist/boards/columns/<int:id>",
        "todolist.board_column.single",
    )
