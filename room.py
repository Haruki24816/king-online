from player import Player


class Room:

    def __init__(self, room_name):
        if len(room_name) == 0:
            raise Exception("部屋の名前は1文字以上でなければなりません")

        if 100 < len(room_name):
            raise Exception("部屋の名前は100文字以下でなければなりません")

        self.name = room_name
        self.players = []

    def add_player(self, player_name):
        for player in self.players:
            if player_name == player.name:
                raise Exception("すでに同じ名前のプレイヤーがいます")
        
        self.players.append(Player(player_name))
        return len(self.players) - 1
    
    def leave(self, player_id):
        self.players[player_id].leave()
    
    def offline(self, player_id):
        self.players[player_id].offline()
    
    def is_offline(self, player_id):
        return self.players[player_id].is_offline()
    
    def reconnect(self, player_id):
        return self.players[player_id].reconnect()
