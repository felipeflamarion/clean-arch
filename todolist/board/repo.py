from json import dumps, loads

from core.response import HttpStatus, ItemResp, ItemsResp
from pendulum import DateTime
from sqlalchemy.exc import IntegrityError
from todolist.entities import Board
from todolist.models import SQLBoard
from todolist.board.interfaces import IBoardRepo


class SQLBoardRepo(IBoardRepo):
    def __init__(self, session):
        self.session = session

    def insert_board(self, board: Board) -> ItemResp:
        sql_board = board_to_db(board)

        try:
            self.session.add(sql_board)
            self.session.commit()
        except IntegrityError:
            return ItemResp(status=HttpStatus.CONFLICT, errors=[])

        board = db_to_board(sql_board)
        return ItemResp(item=board)

    def update_board(self, board: Board) -> ItemResp:
        db_board = board_to_db(board)

        try:
            self.session.query(SQLBoard).filter_by(id=board.id).update(
                {"title": db_board.title, "updated_at": db_board.updated_at}
            )
            self.session.commit()
        except IntegrityError:
            return ItemResp(status=HttpStatus.CONFLICT, errors=[])

        return ItemResp(item=board)

    def get_boards(self) -> ItemsResp:
        db_boards = self.session.query(SQLBoard).all()
        return ItemsResp(items=[db_to_board(db_board) for db_board in db_boards])

    def get_board_by_id(self, id: int) -> ItemResp:
        db_board = self.session.query(SQLBoard).get(id)
        if not db_board:
            return ItemResp(status=HttpStatus.NOT_FOUND)

        return ItemResp(item=db_to_board(db_board))

    def delete_board(self, id: int) -> ItemResp:
        db_board = self.session.query(SQLBoard).get(id)
        if not db_board:
            return ItemResp(status=HttpStatus.NOT_FOUND)

        try:
            self.session.delete(db_board)
            self.session.commit()
        except IntegrityError:
            return ItemResp(status=HttpStatus.CONFLICT)

        return ItemResp()


def board_to_db(board: Board) -> SQLBoard:
    return SQLBoard(
        id=board.id,
        title=board.title,
        created_at=board.created_at,
        updated_at=board.updated_at,
    )


def db_to_board(sql_board: SQLBoard) -> Board:
    return Board(
        id=sql_board.id,
        title=sql_board.title,
        created_at=sql_board.created_at,
        updated_at=sql_board.updated_at,
    )
