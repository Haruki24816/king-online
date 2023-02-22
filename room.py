from errors import EventError0


class Room:

    def __init__(self, room_name):
        self.name = room_name
        self.players = []

    def add_player(self, player_name, sid):
        for player_data in self.players:
            if player_data["name"] == player_name and player_data["status"] != "left":
                raise EventError0("s0-error-same-player-name")

        self.players.append({
            "name": player_name,
            "status": "online",  # online, offline, left
            "sid": sid
        })

        return len(self.players) - 1

    def leave(self, player_id):
        self.players[player_id]["status"] = "left"
        self.update_sid(player_id, None)

    def offline(self, player_id):
        self.players[player_id]["status"] = "offline"
        self.update_sid(player_id, None)

    def player_status(self, player_id):
        return self.players[player_id]["status"]

    def reconnect(self, player_id, sid):
        status = self.players[player_id]["status"]

        if status == "left":
            return False
        else:
            self.update_sid(player_id, sid)
            self.players[player_id]["status"] = "online"
            return True

    def info(self):
        return {
            "room_name": self.name,
            "player_num": self.player_num()
        }

    def player_num(self):
        num = 0

        for player_data in self.players:
            if player_data["status"] != "left":
                num += 1

        return num

    def owner_exists(self):
        return self.players[0]["status"] != "left"

    def update_sid(self, player_id, sid):
        self.players[player_id]["sid"] = sid

    def get_sid(self, player_id):
        return self.players[player_id]["sid"]
