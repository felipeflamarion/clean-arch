from core.bases.api import APIBase
from flask import request
from todolist.ticket.requests import CreateTicket, DeleteTicket, GetTicket, UpdateTicket


class TicketListAPI(APIBase):
    def __init__(self, use_cases, *args, **kwargs):
        self.use_cases = use_cases
        super().__init__(*args, **kwargs)

    def set_methods(self):
        return {"GET": self.get, "POST": self.create}

    def get(self, *args, **kwargs):
        resp = self.use_cases.get_tickets()

        return {
            "tickets": [item.to_json() for item in resp.items]
            if resp.is_ok
            else resp.dump_errors()
        }, resp.status

    def create(self, *args, **kwargs):
        resp = self.use_cases.create_ticket(
            CreateTicket(
                board_id=request.json.get("board_id"),
                title=request.json.get("title"),
                description=request.json.get("description"),
                labels=request.json.get("labels"),
            )
        )

        return resp.item.to_json() if resp.is_ok else resp.dump_errors(), resp.status


class TicketSingleAPI(APIBase):
    def __init__(self, use_cases, *args, **kwargs):
        self.use_cases = use_cases
        super().__init__(*args, **kwargs)

    def set_methods(self):
        return {"GET": self.get_by_id, "PUT": self.update, "DELETE": self.delete}

    def get_by_id(self, id: int):
        resp = self.use_cases.get_ticket(GetTicket(id=id))

        return resp.item.to_json() if resp.is_ok else resp.dump_errors(), resp.status

    def update(self, id: int):
        resp = self.use_cases.update_ticket(
            CreateTicket(
                id=id,
                title=request.json.get("title"),
                description=request.json.get("description"),
                labels=request.json.get("labels"),
            )
        )

        return resp.item.to_json() if resp.is_ok else resp.dump_errors(), resp.status

    def delete(self, id: int):
        resp = self.use_cases.delete_ticket(DeleteTicket(id=id))

        return {} if resp.is_ok else resp.dump_errors(), resp.status


def register_routes(app, use_cases):
    ticket_list_api = TicketListAPI(use_cases)
    ticket_single_api = TicketSingleAPI(use_cases)

    ticket_list_api.register_api(
        app,
        "/api/todolist/tickets",
        "todolist.tickets.list",
    )
    ticket_single_api.register_api(
        app,
        "/api/todolist/tickets/<int:id>",
        "todolist.tickets.single",
    )
