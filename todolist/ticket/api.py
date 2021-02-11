from core.bases.api import APIBase
from flask import request


class TicketListAPI(APIBase):
    def __init__(self, use_cases, *args, **kwargs):
        self.use_cases = use_cases
        super().__init__(*args, **kwargs)

    def set_methods(self):
        return {"GET": self.get, "POST": self.create}

    def get(self, *args, **kwargs):
        resp = self.use_cases.get_tickets()

        return {
            "tickets": [item.to_json() for item in resp.items] if resp.items else []
        }

    def create(self, *args, **kwargs):
        resp = self.use_cases.create_ticket(data=request.json)

        return resp.item.to_json() if resp.item else {}


class TicketSingleAPI(APIBase):
    def __init__(self, use_cases, *args, **kwargs):
        self.use_cases = use_cases
        super().__init__(*args, **kwargs)

    def set_methods(self):
        return {"GET": self.get_by_id, "PUT": self.update, "DELETE": self.delete}

    def get_by_id(self, id: int):
        resp = self.use_cases.get_ticket(id=id)

        return resp.item.to_json() if resp.item else {}

    def update(self, id: int):
        resp = self.use_cases.update_ticket(id=id, data=request.json)

        return resp.item.to_json() if resp.item else {}

    def delete(self, id: int):
        self.use_cases.delete_ticket(id=id)

        return {}


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
