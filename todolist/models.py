import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SQLBoard(Base):
    __tablename__ = "todolist_boards"

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(length=128), nullable=False)
    created_at = sa.Column(sa.DateTime)
    updated_at = sa.Column(sa.DateTime)


class SQLBoardColumn(Base):
    __tablename__ = "todolist_board_columns"

    id = sa.Column(sa.Integer, primary_key=True)
    board_id = sa.Column(
        sa.Integer, sa.ForeignKey("todolist_boards.id"), nullable=False
    )
    name = sa.Column(sa.String(length=32), nullable=False)
    created_at = sa.Column(sa.DateTime)
    updated_at = sa.Column(sa.DateTime)


class SQLPerson(Base):
    __tablename__ = "todolist_persons"

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(length=32), nullable=False)
    display_name = sa.Column(sa.String(length=128), nullable=False)
    email = sa.Column(sa.String(length=128), nullable=False)
    created_at = sa.Column(sa.DateTime)
    updated_at = sa.Column(sa.DateTime)


class SQLTicket(Base):
    __tablename__ = "todolist_tickets"

    id = sa.Column(sa.Integer, primary_key=True)
    board_column_id = sa.Column(
        sa.Integer, sa.ForeignKey("todolist_board_columns.id"), nullable=True
    )
    person_id = sa.Column(
        sa.Integer, sa.ForeignKey("todolist_persons.id"), nullable=True
    )
    title = sa.Column(sa.String(length=128), nullable=False)
    description = sa.Column(sa.Text, nullable=True)
    priority = sa.Column(sa.Integer, nullable=False, default=0)
    labels = sa.Column(sa.Text)
    created_at = sa.Column(sa.DateTime)
    updated_at = sa.Column(sa.DateTime)
