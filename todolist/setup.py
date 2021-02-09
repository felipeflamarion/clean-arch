from todolist.ticket.api import register_routes as register_ticket_routes
from todolist.ticket.repo import SQLTicketRepo
from todolist.ticket.use_cases import TicketUseCases


def setup(app: object):
    session = None

    sql_ticket_repo = SQLTicketRepo(session)
    ticket_use_cases = TicketUseCases(sql_ticket_repo)
    register_ticket_routes(app, ticket_use_cases)
