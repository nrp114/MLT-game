class Room:
    def __init__(self, id):
        self.id = id
        self.clients = []

    def add_client(self, client_id):
        self.clients.append(client_id)