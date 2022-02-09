class Room:

    def __init__(self, name):
        if name in ("", None):
            name = "名前のない部屋"

        self.name = name
        self.status = "wanted"
        self.players = {}
        self.deck = []
