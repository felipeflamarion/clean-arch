from abc import ABC, abstractclassmethod

from core.response import ItemResp, ItemsResp
from todolist.entities import Ticket
from todolist.ticket.requests import CreateTicket, DeleteTicket, GetTicket, UpdateTicket


class ITicketRepo(ABC):
    @abstractclassmethod
    def insert_ticket(self, ticket: Ticket) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def update_ticket(self, ticket: Ticket) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def get_tickets(self) -> ItemsResp:
        raise NotImplementedError

    @abstractclassmethod
    def get_ticket_by_id(self, id: int) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def delete_ticket(self, id: int) -> ItemResp:
        raise NotImplementedError


class ITicketUseCases:
    @abstractclassmethod
    def create_ticket(self, req: CreateTicket) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def update_ticket(self, req: UpdateTicket) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def get_ticket(self, req: GetTicket) -> ItemResp:
        raise NotImplementedError

    @abstractclassmethod
    def get_tickets(self) -> ItemsResp:
        raise NotImplementedError

    @abstractclassmethod
    def delete_ticket(self, req: DeleteTicket) -> ItemResp:
        raise NotImplementedError
