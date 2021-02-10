import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SQLTicket(Base):
    __tablename__ = "todolist_tickets"

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(length=128), nullable=False)
    description = sa.Column(sa.Text, nullable=True)
    labels = sa.Column(sa.Text)
    creation_date = sa.Column(sa.DateTime)
