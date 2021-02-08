from todolist.ticket.api import register_routes as register_ticket_routes
from todolist.ticket.use_cases import TicketUseCases


def setup(app: object):
    ticket_repo = None
    ticket_use_cases = TicketUseCases(ticket_repo)
    register_ticket_routes(app, ticket_use_cases)
