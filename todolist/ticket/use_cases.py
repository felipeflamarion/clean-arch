import pendulum as datetime
from core.response import HttpStatus, ItemResp
from core.validations import handle_validations
from todolist.board.interfaces import IBoardUseCases
from todolist.entities import Ticket
from todolist.ticket import bussiness
from todolist.ticket.interfaces import ITicketRepo, ITicketUseCases
from todolist.ticket.requests import CreateTicket, DeleteTicket, GetTicket, UpdateTicket


class TicketUseCases(ITicketUseCases):
    def __init__(self, repo: ITicketRepo, boards_uc: IBoardUseCases):
        self.repo = repo
        self.boards_uc = boards_uc

    def create_ticket(self, req: CreateTicket):
        resp = handle_validations(
            [
                bussiness.validate_board_id(req.board_id, self.boards_uc),
                bussiness.validate_title(req.title),
                bussiness.validate_description(req.description),
                bussiness.validate_labels(req.labels),
            ]
        )
        if not resp.is_ok:
            return resp

        ticket = Ticket(
            board_id=req.board_id,
            title=req.title,
            description=req.description,
            labels=req.labels,
            creation_date=datetime.now(),
        )
        return self.repo.insert_ticket(ticket)

    def update_ticket(self, req: UpdateTicket):
        resp = self.repo.get_ticket_by_id(id=req.id)
        if not resp.item:
            return resp
        ticket = resp.item

        resp = handle_validations(
            [
                bussiness.validate_title(req.title),
                bussiness.validate_description(req.description),
                bussiness.validate_labels(req.labels),
            ]
        )
        if not resp.is_ok:
            return resp

        ticket = Ticket(
            id=req.id,
            title=req.title,
            description=req.description,
            labels=req.labels,
            creation_date=ticket.creation_date,
        )
        return self.repo.update_ticket(ticket)

    def get_ticket(self, req: GetTicket):
        return self.repo.get_ticket_by_id(id=req.id)

    def get_tickets(self):
        return self.repo.get_tickets()

    def delete_ticket(self, req: DeleteTicket):
        return self.repo.delete_ticket(id=req.id)
