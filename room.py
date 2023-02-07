class Room:

    def __init__(self, room_name):
        if len(room_name) == 0:
            raise Exception("部屋の名前は1文字以上でなければなりません")

        if 100 < len(room_name):
            raise Exception("部屋の名前は100文字以下でなければなりません")

        self.name = room_name
        self.players = []

    def add_player(self, player_name):
        for player_data in self.players:
            if player_data["name"] == player_name:
                raise Exception("すでに同じ名前のプレイヤーがいます")

        if len(player_name) == 0:
            raise Exception("プレイヤー名は1文字以上でなければなりません")

        if 100 < len(player_name):
            raise Exception("プレイヤー名は100文字以下でなければなりません")

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
