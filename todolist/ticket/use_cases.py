class TicketUseCases:
    def __init__(self, repo):
        self.repo = repo

    def create_ticket(self, data: dict):
        ticket = data  # TODO: call bussiness rules validation
        return self.repo.create_ticket(ticket)

    def update_ticket(self, id: int, data: dict):
        ticket = {**data, "id": id}
        return self.repo.update_ticket(ticket)

    def get_ticket(self, id: int):
        return self.repo.get_ticket_by_id(id=id)

    def get_tickets(self):
        return self.repo.get_tickets()

    def delete_ticket(self, id: int):
        return self.repo.delete_ticket(id=id)
