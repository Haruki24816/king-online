from errors import EventError0


class Room:

    def __init__(self, room_name):
        self.name = room_name
        self.players = []

    def add_player(self, player_name):
        for player_data in self.players:
            if player_data["name"] == player_name and player_data["status"] != "left":
                raise EventError0("s0-error-same-player-name")

        self.players.append({
            "name": player_name,
            "status": "online" # online, offline, left
        })

        return len(self.players) - 1

    def leave(self, player_id):
        self.players[player_id]["status"] = "left"

    def offline(self, player_id):
        self.players[player_id]["status"] = "offline"

    def is_offline(self, player_id):
        return self.players[player_id]["status"] == "offline"

    def reconnect(self, player_id):
        status = self.players[player_id]["status"]

        if status == "left":
            return False
        else:
            status = "online"
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
