from json import dumps, loads

from core.response import HttpStatus, ItemResp, ItemsResp
from pendulum import DateTime
from sqlalchemy.exc import IntegrityError
from todolist.entities import Ticket
from todolist.models import SQLTicket
from todolist.ticket.interfaces import ITicketRepo


class SQLTicketRepo(ITicketRepo):
    def __init__(self, session):
        self.session = session

    def insert_ticket(self, ticket: Ticket) -> ItemResp:
        sql_ticket = ticket_to_db(ticket)

        try:
            self.session.add(sql_ticket)
            self.session.commit()
        except IntegrityError:
            return ItemResp(status=HttpStatus.CONFLICT, errors=[])

        ticket = db_to_ticket(sql_ticket)
        return ItemResp(item=ticket)

    def update_ticket(self, ticket: Ticket) -> ItemResp:
        db_ticket = ticket_to_db(ticket)

        try:
            self.session.query(SQLTicket).filter_by(id=ticket.id).update(
                {
                    "title": db_ticket.title,
                    "description": db_ticket.description,
                    "priority": db_ticket.priority,
                    "labels": db_ticket.labels,
                    "updated_at": db_ticket.updated_at,
                }
            )
            self.session.commit()
        except IntegrityError:
            return ItemResp(status=HttpStatus.CONFLICT, errors=[])

        return ItemResp(item=ticket)

    def get_tickets(self) -> ItemsResp:
        db_tickets = self.session.query(SQLTicket).all()
        return ItemsResp(items=[db_to_ticket(db_ticket) for db_ticket in db_tickets])

    def get_ticket_by_id(self, id: int) -> ItemResp:
        db_ticket = self.session.query(SQLTicket).get(id)
        if not db_ticket:
            return ItemResp(status=HttpStatus.NOT_FOUND)

        return ItemResp(item=db_to_ticket(db_ticket))

    def delete_ticket(self, id: int) -> ItemResp:
        db_ticket = self.session.query(SQLTicket).get(id)
        if not db_ticket:
            return ItemResp(status=HttpStatus.NOT_FOUND)

        try:
            self.session.delete(db_ticket)
            self.session.commit()
        except IntegrityError:
            return ItemResp(status=HttpStatus.CONFLICT)

        return ItemResp()


def ticket_to_db(ticket: Ticket) -> SQLTicket:
    return SQLTicket(
        id=ticket.id,
        board_column_id=ticket.board_column_id,
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
        labels=dumps(ticket.labels),
        created_at=ticket.created_at,
        updated_at=ticket.updated_at,
    )


def db_to_ticket(sql_ticket: SQLTicket) -> Ticket:
    return Ticket(
        id=sql_ticket.id,
        board_column_id=sql_ticket.board_column_id,
        title=sql_ticket.title,
        description=sql_ticket.description,
        priority=sql_ticket.priority,
        labels=loads(sql_ticket.labels) if sql_ticket.labels else [],
        created_at=sql_ticket.created_at,
        updated_at=sql_ticket.updated_at,
    )
