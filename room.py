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
            "name": "",    #プレイヤー名
            "status": 0,   #プレイヤーのステータス 未準備：0 準備完了：1 ゲーム中：2
            "hand": None,  #手札 辞書
            "debt": None,  #借金 辞書
            "drawn": None, #引いた額 整数
            "paid": None   #支払った額 整数
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
            player["drawn"] = 0
            player["paid"] = 0

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
            player["drawn"] = None
            player["paid"] = None

        self.status = 0
        self.deck = None
        self.order = None
        self.turn = None
        self.is_payment_waiting = None

    def draw_fifteen(self, sid, *, red=0, green=0, blue=0):
        sid = str(sid)
        red = int(red)
        green = int(green)
        blue = int(blue)

        if self.status != -1:
            raise Exception("カードを引けません")

        if self.order[self.turn] != sid:
            raise ValueError("このプレイヤーの番ではありません")

        if (red+green+blue) not in (0, 15):
            raise ValueError("無効な値です")

        red_cards = []
        green_cards = []
        blue_cards = []
        for kind, card_num in self.deck.items():
            if kind[0] == "r":
                for num in range(card_num):
                    red_cards.append(kind)
            if kind[0] == "g":
                for num in range(card_num):
                    green_cards.append(kind)
            if kind[0] == "r":
                for num in range(card_num):
                    blue_cards.append(kind)

        if (red+green+blue) == 0:
            all_cards = red_cards + green_cards + blue_cards
            chosen_cards = random.sample(all_cards, 15)
        else:
            chosen_red_cards = random.sample(red_cards, red)
            chosen_green_cards = random.sample(green_cards, green)
            chosen_blue_cards = random.sample(blue_cards, blue)
            chosen_cards = chosen_red_cards + chosen_green_cards + chosen_blue_cards

        for card in chosen_cards:
            if card not in self.players[sid]["hand"]:
                self.players[sid]["hand"][card] = 0
            self.players[sid]["hand"][card] += 1
            self.deck[card] -= 1
            if self.deck[card] == 0:
                self.deck.pop(card)

        self.turn += 1

        if self.turn == len(self.order):
            self.turn = 0
            self.status = 1

    def draw(self, sid, color=None):
        sid = str(sid)
        color = str(color)

        if self.status < 1:
            raise Exception("カードを引けません")

        if self.is_payment_waiting:
            raise Exception("カードを引けません")

        if self.order[self.turn] != sid:
            raise ValueError("このプレイヤーの番ではありません")

        if color not in ("r", "g", "b", "None"):
            raise ValueError("無効な値です")

        if color == "None":
            colors = ("r", "g", "b")
        else:
            colors = (color)

        cards = []
        for kind, card_num in self.deck.items():
            if kind[0] in colors:
                for num in range(card_num):
                    cards.append(kind)

        chosen_card = random.choice(cards)

        if chosen_card not in self.players[sid]["hand"]:
            self.players[sid]["hand"][chosen_card] = 0

        self.players[sid]["hand"][chosen_card] += 1
        self.deck[chosen_card] -= 1

        if self.deck[chosen_card] == 0:
            self.deck.pop(chosen_card)

        if chosen_card[1] == "1":
            self.players[sid]["drawn"] = 100
        if chosen_card[1] == "5":
            self.players[sid]["drawn"] = 500
        if chosen_card[1] == "k":
            self.players[sid]["drawn"] = 500
        if chosen_card[1] == "a":
            self.players[sid]["drawn"] = 1000
        if chosen_card[1] == "j":
            self.players[sid]["drawn"] = 2000

        self.is_payment_waiting = True

    def pay(self, sid, **cards):
        sid = str(sid)
        turn_sid = self.order[self.turn]

        if self.status < 1:
            raise Exception("支払いできません")

        if not self.is_payment_waiting:
            raise Exception("支払いできません")

        if turn_sid == sid:
            raise ValueError("カードを引いたプレイヤーです")

        for kind, num in cards.items():
            if kind not in self.players[sid]["hand"]:
                raise ValueError("持っていないカードがあります")
            if self.players[sid]["hand"][kind] < num:
                raise ValueError("枚数が足りません")

        if cards == {}:
            for kind in self.players[sid]["hand"]:
                if kind[1] == "1":
                    break
            else:
                raise ValueError("100円がありません")
            cards = {kind: 1}

        payment_amount = 0
        for kind, num in cards.items():
            if kind[1] == "1":
                payment_amount += (100*num)
            if kind[1] == "5":
                payment_amount += (500*num)
            if kind[1] == "k":
                payment_amount += (500*num)
            if kind[1] == "a":
                payment_amount += (1000*num)
            if kind[1] == "j":
                payment_amount += (2000*num)

        paid_amount = self.players[sid]["paid"]
        drawn_amount = self.players[turn_sid]["drawn"]

        if (payment_amount+paid_amount) > drawn_amount:
            raise ValueError("金額が多すぎます")

        for kind, num in cards.items():
            self.players[sid]["hand"][kind] -= num
            if self.players[sid]["hand"][kind] == 0:
                self.players[sid]["hand"].pop(kind)
            if kind in self.players[turn_sid]["hand"]:
                self.players[turn_sid]["hand"][kind] = 0
            self.players[turn_sid]["hand"][kind] += num
            self.players[sid]["paid"] += payment_amount

        count = 0
        for key, value in self.players.items():
            if key == turn_sid:
                continue
            if value["paid"] != self.players[turn_sid]["drawn"]:
                count += 1

        if count == 0:
            for player in self.players.values():
                player["drawn"] = 0
                player["paid"] = 0
            self.turn += 1
            self.is_payment_waiting = False
            if self.turn == len(self.order):
                self.turn = 0
                self.status += 1
