import random


class Room:

    def __init__(self, name):
        name = str(name)

        if name in ("", "None"):
            name = "名前のない部屋"

        self.name = name  #部屋の名前
        self.status = 0   #部屋のステータス 募集中：0 準備中：-1 返済待ち：-2 ゲーム終了時：-3 ゲーム中：1以上（周数）
        self.players = {} #プレイヤー情報

        self.deck = None               #山札 辞書
        self.order = None              #プレイヤーの順番 sidのリスト
        self.turn = None               #順番 整数
        self.is_payment_waiting = None #支払い待ちかどうか

    def info(self):
        data = {
            "room_name": self.name,
            "room_status": self.status,
            "players": self.players,
            "deck": self.deck,
            "order": self.order,
            "turn": self.turn,
            "is_payment_waiting": self.is_payment_waiting
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
            "hand": None, #手札 辞書
            "debt": None  #借金 辞書
        }

    def remove_player(self, sid):
        sid = str(sid)
        self.players.pop(sid)

        try:
            if self.status == 0:
                self.prepare()
            else:
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
            player["hand"] = {}
            player["debt"] = {}

        self.deck = {}
        for color in ("r", "g", "b"):
            self.deck[color + "1"] = 36
            self.deck[color + "5"] = 8
            self.deck[color + "k"] = 4
            self.deck[color + "a"] = 4

        self.order = list(self.players.keys())
        random.shuffle(self.order)

        self.status = -1
        self.turn = 0
        self.is_payment_waiting = False

    def finish(self):
        if self.status == 0:
            raise Exception("ゲーム進行中ではありません")

        for player in self.players.values():
            player["status"] = 0
            player["hand"] = None
            player["debt"] = None

        self.status = 0
        self.deck = None
        self.order = None
        self.turn = None
        self.is_payment_waiting = None

    def draw(self, sid, color=None):
        sid = str(sid)
        color = str(color)

        if self.status in (0, -2, -3):
            raise Exception("カードを引けません")

        if color not in ("r", "g", "b", "None"):
            raise ValueError("無効な値です")

        if self.order[self.turn] != sid:
            raise ValueError("このプレイヤーの番ではありません")

        if self.is_payment_waiting:
            raise Exception("カードを引けません")

        if color == "None":
            colors = ("r", "g", "b")
        else:
            colors = (color)

        unpacked_deck = []
        for kind, card_num in self.deck.items():
            if kind[0] in colors:
                for num in range(card_num):
                    unpacked_deck.append(kind)

        chosen_kind = random.choice(unpacked_deck)

        if chosen_kind not in self.players[sid]["hand"]:
            self.players[sid]["hand"][chosen_kind] = 0

        self.players[sid]["hand"][chosen_kind] += 1
        self.deck[chosen_kind] -= 1

        if self.deck[chosen_kind] == 0:
            self.deck.pop(chosen_kind)

        if self.status > 0:
            self.is_payment_waiting = True

        if self.status == -1:
            count = 0
            for num in self.players[sid]["hand"].values():
                count += num
            if count == 15:
                self.turn += 1
            if self.turn == len(self.order):
                self.turn = 0
                self.status = 1
