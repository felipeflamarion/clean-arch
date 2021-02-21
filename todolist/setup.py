from todolist.board.api import register_routes as register_board_routes
from todolist.board.repo import SQLBoardRepo
from todolist.board.use_cases import BoardUseCases
from todolist.ticket.api import register_routes as register_ticket_routes
from todolist.ticket.repo import SQLTicketRepo
from todolist.ticket.use_cases import TicketUseCases


def setup(app: object, session):
    sql_board_repo = SQLBoardRepo(session)
    board_use_cases = BoardUseCases(sql_board_repo)
    register_board_routes(app, board_use_cases)

    sql_ticket_repo = SQLTicketRepo(session)
    ticket_use_cases = TicketUseCases(sql_ticket_repo, boards_uc=board_use_cases)
    register_ticket_routes(app, ticket_use_cases)
