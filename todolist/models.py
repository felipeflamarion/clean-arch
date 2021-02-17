import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SQLBoard(Base):
    __tablename__ = "todolist_boards"

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(length=128), nullable=False)
    creation_date = sa.Column(sa.DateTime)


class SQLTicket(Base):
    __tablename__ = "todolist_tickets"

    id = sa.Column(sa.Integer, primary_key=True)
    board_id = sa.Column(
        sa.Integer, sa.ForeignKey("todolist_boards.id"), nullable=False
    )
    title = sa.Column(sa.String(length=128), nullable=False)
    description = sa.Column(sa.Text, nullable=True)
    labels = sa.Column(sa.Text)
    creation_date = sa.Column(sa.DateTime)
