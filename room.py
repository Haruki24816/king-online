import random


class Room:

    def __init__(self, name):
        if name in ("", None):
            name = "名前のない部屋"

        self.name = name     #部屋の名前
        self.in_game = False #ゲーム中かどうか
        self.players = {}    #プレイヤー情報

        self.deck = None               #山札 リスト
        self.lap = None                #周 数 15枚引くのを待つときは-1 返済待ちのときは-2
        self.order = None              #プレイヤーの順番 sidのリスト
        self.turn = None               #順番 数
        self.is_payment_waiting = None #支払い待ちかどうか

    def add_player(self, sid):
        self.players[sid] = {
            "name": "",        #プレイヤー名
            "is_ready": False, #準備ができているか
            "hand": None,      #手札 リスト
            "debt": None       #借金 辞書
        }

    def remove_player(self, sid):
        self.players.pop(sid)
        self.prepare()

    def register_player_name(self, sid, name):
        name = name.rstrip("′")

        count = 0
        for value in self.players.values():
            if value["name"].rstrip("′") == name:
                count += 1

        for num in range(count):
            name += "′"

        self.players[sid]["name"] = name

    def ready(self, sid):
        self.players[sid]["is_ready"] = True
        self.prepare()

    def prepare(self):
        if len(self.players) < 2:
            return

        count = 0
        for value in self.players.values():
            if not value["is_ready"]:
                count += 1

        if count != 0:
            return

        for value in self.players.values():
            value["is_ready"] = False
            value["hand"] = []
            value["debt"] = {}

        self.deck = []
        for color in ("r", "g", "b"):
            for num in range(36):
                self.deck.append(color + "1")
            for num in range(8):
                self.deck.append(color + "5")
            for num in range(4):
                self.deck.append(color + "k")
            for num in range(4):
                self.deck.append(color + "a")

        self.order = list(self.players.keys())
        random.shuffle(self.order)

        self.in_game = True
        self.lap = -1
        self.turn = 0
        self.is_payment_waiting = False
