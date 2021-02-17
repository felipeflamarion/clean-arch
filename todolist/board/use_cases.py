import pendulum as datetime
from core.response import HttpStatus, ItemResp
from todolist.entities import Board


class BoardUseCases:
    def __init__(self, repo):
        self.repo = repo

    def create_board(self, data: dict):
        board = Board(
            title=data.get("title"),
            creation_date=datetime.now(),
        )
        return self.repo.insert_board(board)

    def update_board(self, id: int, data: dict):
        resp = self.get_board(id=id)
        if not resp.item:
            return resp

        board = Board(
            id=id,
            title=data.get("title"),
            creation_date=resp.item.creation_date,
        )
        return self.repo.update_board(board)

    def get_board(self, id: int):
        return self.repo.get_board_by_id(id=id)

    def get_boards(self):
        return self.repo.get_boards()

    def delete_board(self, id: int):
        return self.repo.delete_board(id=id)
