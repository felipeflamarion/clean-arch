import pendulum as datetime
from core.response import HttpStatus, ItemResp
from core.validations import handle_validations
from todolist.board_column.interfaces import IBoardColumnUseCases
from todolist.entities import Ticket
from todolist.ticket import bussiness, validations
from todolist.ticket.interfaces import ITicketRepo, ITicketUseCases
from todolist.ticket.requests import CreateTicket, DeleteTicket, GetTicket, UpdateTicket


class TicketUseCases(ITicketUseCases):
    def __init__(self, repo: ITicketRepo, board_columns_uc: IBoardColumnUseCases):
        self.repo = repo
        self.board_columns_uc = board_columns_uc

    def create_ticket(self, req: CreateTicket):
        resp = handle_validations(
            fields_validations=[
                validations.validate_board_column_id(req.board_column_id),
                validations.validate_title(req.title),
                validations.validate_description(req.description),
                validations.validate_priority(req.priority),
                validations.validate_labels(req.labels),
            ],
            bussiness_validations=[
                bussiness.validate_board_column_id(
                    req.board_column_id, self.board_columns_uc
                )
            ],
        )
        if not resp.is_ok:
            return resp

        created_at = datetime.now()

        ticket = Ticket(
            board_column_id=req.board_column_id,
            title=req.title,
            description=req.description,
            priority=req.priority,
            labels=req.labels if req.labels is not None else [],
            created_at=created_at,
            updated_at=created_at,
        )
        return self.repo.insert_ticket(ticket)

    def update_ticket(self, req: UpdateTicket):
        resp = self.repo.get_ticket_by_id(id=req.id)
        if not resp.item:
            return resp
        ticket = resp.item

        resp = handle_validations(
            fields_validations=[
                validations.validate_title(req.title),
                validations.validate_description(req.description),
                validations.validate_priority(req.priority),
                validations.validate_labels(req.labels),
            ],
        )
        if not resp.is_ok:
            return resp

        updated_at = datetime.now()

        ticket = Ticket(
            id=req.id,
            board_column_id=ticket.board_column_id,
            title=req.title,
            description=req.description,
            priority=req.priority,
            labels=req.labels if req.labels is not None else [],
            created_at=ticket.created_at,
            updated_at=updated_at,
        )
        return self.repo.update_ticket(ticket)

    def get_ticket(self, req: GetTicket):
        return self.repo.get_ticket_by_id(id=req.id)

    def get_tickets(self):
        return self.repo.get_tickets()

    def delete_ticket(self, req: DeleteTicket):
        return self.repo.delete_ticket(id=req.id)
