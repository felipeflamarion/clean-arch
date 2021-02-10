from core.response import ItemResp, ItemsResp
from pendulum import DateTime
from todolist.entities import Ticket
from todolist.models import SQLTicket
from todolist.ticket.interfaces import ITicketRepo


class SQLTicketRepo(ITicketRepo):
    def __init__(self, session):
        self.session = session

    def insert_ticket(self, ticket: Ticket) -> ItemResp:
        raise NotImplementedError

    def update_ticket(self, ticket: Ticket) -> ItemResp:
        raise NotImplementedError

    def get_tickets(self) -> ItemsResp:
        ticket = Ticket(
            id=1,
            title="Ticket01",
            description="There is a test ticket",
            labels=["test", "clean", "arch"],
            creation_date=DateTime(2020, 2, 9, 15, 0, 0),
        )
        return ItemsResp(items=[ticket])

    def get_ticket_by_id(self, id: int) -> ItemResp:
        raise NotImplementedError

    def delete_ticket(self, id: int) -> ItemResp:
        raise NotImplementedError


def ticket_to_db(ticket: Ticket) -> SQLTicket:
    return


def db_to_ticket(sql_ticket: SQLTicket) -> Ticket:
    return
