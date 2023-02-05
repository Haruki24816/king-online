class Player:

    def __init__(self, player_name):
        if len(player_name) == 0:
            raise Exception("プレイヤー名は1文字以上でなければなりません")

        if 100 < len(player_name):
            raise Exception("プレイヤー名は100文字以下でなければなりません")
        
        self.name = player_name
        self.status = "online" # online, offline, left
    
    def leave(self):
        self.status = "left"
    
    def offline(self):
        self.status = "offline"

    def is_offline(self):
        return self.status == "offline"

    def reconnect(self):
        if self.status == "left":
            return False
        else:
            self.status = "online"
            return True
