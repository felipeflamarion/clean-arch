import pendulum as datetime
from core.response import HttpStatus, ItemResp
from todolist.entities import Ticket


class TicketUseCases:
    def __init__(self, repo):
        self.repo = repo

    def create_ticket(self, data: dict):
        ticket = Ticket(
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

        ticket = Ticket(
            id=id,
            title=data.get("title"),
            description=data.get("description"),
            labels=data.get("labels"),
            creation_date=resp.item.creation_date,
        )
        return self.repo.update_ticket(ticket)

    def get_ticket(self, id: int):
        return self.repo.get_ticket_by_id(id=id)

    def get_tickets(self):
        return self.repo.get_tickets()

    def delete_ticket(self, id: int):
        return self.repo.delete_ticket(id=id)
