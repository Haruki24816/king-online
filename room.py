import random


class Room:

    def __init__(self, name):
        name = str(name)

        if name in ("", "None"):
            name = "名前のない部屋"

        self.name = name  #部屋の名前
        self.status = 0   #部屋のステータス 募集中：0 準備中：-1 返済待ち：-2 ゲーム終了時：-3 ゲーム中：1以上（周数）
        self.players = {} #プレイヤー情報

        self.deck = None  #山札 リスト
        self.order = None #プレイヤーの順番 sidのリスト
        self.turn = None  #順番 整数 支払い待ちのときはマイナス

    def info(self):
        data = {
            "room_name": self.name,
            "room_status": self.status,
            "players": self.players,
            "deck": self.deck,
            "order": self.order,
            "turn": self.turn
        }

        return data

    def add_player(self, sid):
        sid = str(sid)

        if self.status != 0:
            raise Exception("ゲーム進行中のため追加できません")

        if sid in self.players:
            raise ValueError("このプレイヤーはすでに追加されています")

        self.players[sid] = {
            "name": "",   #プレイヤー名
            "status": 0,  #プレイヤーのステータス 未準備：0 準備完了：1 ゲーム中：2
            "hand": None, #手札 リスト
            "debt": None  #借金 辞書
        }

    def remove_player(self, sid):
        sid = str(sid)
        self.players.pop(sid)

        try:
            self.prepare()
        except Exception:
            pass

        try:
            self.finish()
        except Exception:
            pass

    def register_player_name(self, sid, name):
        sid = str(sid)
        name = str(name)

        if self.status != 0:
            raise Exception("ゲーム進行中のため登録できません")

        if name in ("", "None"):
            raise ValueError("無効な名前です")

        if self.players[sid]["name"] != "":
            raise ValueError("このプレイヤーはすでに名前が登録されています")

        for player in self.players.values():
            if player["name"] == name:
                raise ValueError("この名前は他プレイヤーに使われています")

        self.players[sid]["name"] = name

    def update_player_status(self, sid, status):
        sid = str(sid)
        status = int(status)

        if self.status != 0:
            raise Exception("ゲーム進行中のため更新できません")

        if self.players[sid]["name"] == "":
            raise ValueError("このプレイヤーは名前が登録されていません")

        if status not in (0, 1):
            raise ValueError("無効な番号です")

        self.players[sid]["status"] = status

        try:
            self.prepare()
        except Exception:
            pass

    def prepare(self):
        if self.status != 0:
            raise Exception("ゲーム進行中です")

        if len(self.players) < 2:
            raise Exception("プレイヤー人数が足りません")

        count = 0
        for player in self.players.values():
            if player["status"] == 0:
                count += 1

        if count != 0:
            raise Exception("準備ができていないプレイヤーがいます")

        for player in self.players.values():
            player["status"] = 2
            player["hand"] = []
            player["debt"] = {}

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

        self.status = -1
        self.turn = 0

    def finish(self):
        pass
