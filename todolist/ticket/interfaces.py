from abc import ABC, abstractclassmethod

from core.response import ItemResp, ItemsResp
from todolist.entities import Ticket


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
