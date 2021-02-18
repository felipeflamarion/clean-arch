import pendulum as datetime
from core.response import HttpStatus, ItemResp
from core.validations import handle_validations
from todolist.entities import Ticket
from todolist.ticket import bussiness


class TicketUseCases:
    def __init__(self, repo):
        self.repo = repo

    def create_ticket(self, data: dict):
        resp = handle_validations(
            [
                bussiness.validate_board_id(None),
                bussiness.validate_title(None),
                bussiness.validate_description(None),
                bussiness.validate_labels(None),
            ]
        )
        if resp.is_ok:
            return resp

        ticket = Ticket(
            board_id=data.get("board_id"),
            title=data.get("title"),
            description=data.get("description"),
            labels=data.get("labels"),
            creation_date=datetime.now(),
        )
        return self.repo.insert_ticket(ticket)

    def update_ticket(self, id: int, data: dict):
        resp = self.get_ticket(id=id)
        if not resp.item:
            return resp
        ticket = resp.item

        resp = handle_validations(
            [
                bussiness.validate_board_id(None),
                bussiness.validate_title(None),
                bussiness.validate_description(None),
                bussiness.validate_labels(None),
            ]
        )
        if resp.is_ok:
            return resp

        ticket = Ticket(
            id=id,
            title=data.get("title"),
            description=data.get("description"),
            labels=data.get("labels"),
            creation_date=ticket.creation_date,
        )
        return self.repo.update_ticket(ticket)

    def get_ticket(self, id: int):
        return self.repo.get_ticket_by_id(id=id)

    def get_tickets(self):
        return self.repo.get_tickets()

    def delete_ticket(self, id: int):
        return self.repo.delete_ticket(id=id)
