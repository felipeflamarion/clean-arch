class TicketUseCases:
    def __init__(self, repo):
        self.repo = repo

    def create_ticket(self, data: dict):
        print(data)
        return {}

    def update_ticket(self, id: int, data: dict):
        return {}

    def get_ticket(self, id: int):
        print(id)
        return {}

    def get_tickets(self):
        return {"tickets": []}

    def delete_ticket(self, id: int):
        return {}
