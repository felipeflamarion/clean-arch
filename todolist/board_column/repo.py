from json import dumps, loads

from core.response import HttpStatus, ItemResp, ItemsResp
from pendulum import DateTime
from sqlalchemy.exc import IntegrityError
from todolist.board_column.interfaces import IBoardColumnRepo
from todolist.entities import BoardColumn
from todolist.models import SQLBoardColumn


class SQLBoardColumnRepo(IBoardColumnRepo):
    def __init__(self, session):
        self.session = session

    def insert_board_column(self, board_column: BoardColumn) -> ItemResp:
        sql_board_column = board_column_to_db(board_column)

        try:
            self.session.add(sql_board_column)
            self.session.commit()
        except IntegrityError:
            return ItemResp(status=HttpStatus.CONFLICT, errors=[])

        board_column = db_to_board_column(sql_board_column)
        return ItemResp(item=board_column)

    def update_board_column(self, board_column: BoardColumn) -> ItemResp:
        db_board_column = board_column_to_db(board_column)

        try:
            self.session.query(SQLBoardColumn).filter_by(id=board_column.id).update(
                {
                    "name": db_board_column.name,
                    "updated_at": db_board_column.updated_at,
                }
            )
            self.session.commit()
        except IntegrityError:
            return ItemResp(status=HttpStatus.CONFLICT, errors=[])

        return ItemResp(item=board_column)

    def get_board_columns_by_board_id(self, board_id: int) -> ItemsResp:
        db_board_columns = self.session.query(SQLBoardColumn).filter_by(
            board_id=board_id
        )
        return ItemsResp(
            items=[
                db_to_board_column(db_board_column)
                for db_board_column in db_board_columns
            ]
        )

    def get_board_column_by_id(self, id: int) -> ItemResp:
        db_board_column = self.session.query(SQLBoardColumn).get(id)
        if not db_board_column:
            return ItemResp(status=HttpStatus.NOT_FOUND)

        return ItemResp(item=db_to_board_column(db_board_column))

    def delete_board_column(self, id: int) -> ItemResp:
        db_board_column = self.session.query(SQLBoardColumn).get(id)
        if not db_board_column:
            return ItemResp(status=HttpStatus.NOT_FOUND)

        try:
            self.session.delete(db_board_column)
            self.session.commit()
        except IntegrityError:
            return ItemResp(status=HttpStatus.CONFLICT)

        return ItemResp()


def board_column_to_db(board_column: BoardColumn) -> SQLBoardColumn:
    return SQLBoardColumn(
        id=board_column.id,
        board_id=board_column.board_id,
        name=board_column.name,
        created_at=board_column.created_at,
        updated_at=board_column.updated_at,
    )


def db_to_board_column(sql_board_column: SQLBoardColumn) -> BoardColumn:
    return BoardColumn(
        id=sql_board_column.id,
        board_id=sql_board_column.board_id,
        name=sql_board_column.name,
        created_at=sql_board_column.created_at,
        updated_at=sql_board_column.updated_at,
    )
