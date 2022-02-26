import random


class Cards:

    def __init__(self, **cards):
        self.check(cards)
        self.cards = cards

    def check(self, cards):
        for kind, num in cards.items():
            if (len(kind) != 2 or
                kind[0] not in ("r", "g", "b") or
                kind[1] not in ("a", "b", "c", "d", "e")):
                raise ValueError("無効な種類のカードが指定されています")
            if num < 1:
                raise ValueError("無効な枚数が指定されています")

    def add(self, **cards):
        self.check(cards)

        for kind, num in cards.items():
            if kind not in self.cards:
                self.cards[kind] = 0
            self.cards[kind] += num

    def remove(self, **cards):
        self.check(cards)

        for kind, num in cards.items():
            if kind not in self.cards:
                raise ValueError("存在しないカードが指定されています")
            if self.cards[kind] < num:
                raise ValueError("枚数が多すぎます")

        for kind, num in cards.items():
            self.cards[kind] -= num
            if self.cards[kind] == 0:
                self.cards.pop(kind)

    def draw(self, *, red=0, green=0, blue=0):
        red_card_list, green_card_list, blue_card_list = [], [], []

        for kind, num in self.cards.items():
            if kind[0] == "r":
                for n in range(num):
                    red_card_list.append(kind)
            if kind[0] == "g":
                for n in range(num):
                    green_card_list.append(kind)
            if kind[0] == "b":
                for n in range(num):
                    blue_card_list.append(kind)

        card_list = []
        card_list += random.sample(red_card_list, red)
        card_list += random.sample(green_card_list, green)
        card_list += random.sample(blue_card_list, blue)

        cards = {}

        for kind in card_list:
            if kind not in cards:
                cards[kind] = 0
            cards[kind] += 1

        self.remove(**cards)
        return cards

    def card_num(self):
        red_num, green_num, blue_num = 0, 0, 0

        for kind, num in self.cards.items():
            if kind[0] == "r":
                red_num += num
            if kind[0] == "g":
                green_num += num
            if kind[0] == "b":
                blue_num += num

        return {"r": red_num, "g": green_num, "b": blue_num}

    def amount(self, king=False):
        card_value = {"a": 100, "b": 500, "c": 500, "d": 1000, "e": 2000}
        amount = 0

        if king:
            card_value["c"] = -2000

        for kind, num in self.cards.items():
            for letter, value in card_value.items():
                if kind[1] == letter:
                    amount += value * num

        return amount


class Player:

    def __init__(self):
        self.name = ""    #プレイヤー名
        self.status = 0   #プレイヤーのステータス 未準備：0 準備完了：1 ゲーム中：2
        self.hand = None  #手札 Cardsクラス
        self.debts = None #借金 辞書
        self.paid = None  #支払った額

    def prepare(self):
        self.status = 2
        self.hand = Cards()
        self.debt = {}
        self.paid = 0

    def finish(self):
        self.status = 0
        self.hand = None
        self.debt = None
        self.paid = None

    def debt(self, sid, amount):
        if sid not in self.debts:
            self.debts[sid] = 0

        self.debts[sid] += amount

        if self.debts[sid] == 0:
            self.debts.pop(sid)


class Room:

    def __init__(self, name=""):
        if name in ("", None):
            name = "名前のない部屋"

        self.name = name  #部屋の名前
        self.status = 0   #部屋のステータス 募集中：0 準備中：-1 返済待ち：-2 ゲーム終了時：-3 ゲーム中：1以上（週数）
        self.players = {} #プレイヤー情報

        self.deck = None  #山札 Cardsクラス
        self.order = None #順番 セッションIDのリスト
        self.turn = None  #順番の数
        self.drawn = None #引かれた額

    def info(self):
        pass

    def add_player(self, sid):
        if self.status != 0:
            raise Exception("プレイヤーを追加できません")

        if len(self.players) == 8:
            raise Exception("満員です")

        if sid in self.players:
            raise ValueError("すでに登録されているプレイヤーです")

        self.players[sid] = Player()

    def remove_player(self, sid):
        name = self.players[sid].name
        self.players.pop(sid)

        try:
            if self.status == 0:
                self.prepare()
            else:
                self.finish()
        except Exception:
            pass

        return name

    def register_player_name(self, sid, name):
        if self.status != 0:
            raise Exception("プレイヤー名を登録できません")

        if name in ("", None):
            raise ValueError("無効な名前です")

        if self.players[sid].name == name:
            raise ValueError("すでに名前が登録されているプレイヤーです")

        for player in self.players.values():
            if player.name == name:
                raise ValueError("他のプレイヤーに使われている名前です")

        self.players[sid].name = name

    def update_player_status(self, sid, status):
        if self.status == 0:
            if self.players[sid].name == "":
                raise ValueError("名前が登録されていないプレイヤーです")
            if status not in (0, 1):
                raise ValueError("無効な番号です")
        elif self.status == -3:
            if status != 0:
                raise ValueError("無効な番号です")
        else:
            raise Exception("ステータスを更新できません")

        self.players[sid].status = status

        try:
            self.prepare()
        except Exception:
            pass

    def prepare(self):
        if self.status != 0:
            raise Exception("準備できません")

        if len(self.players) < 2:
            raise Exception("プレイヤー人数が足りません")

        for player in self.players.values():
            if player.status == 0:
                raise Exception("準備ができていないプレイヤーがいます")

        for player in self.players.values():
            player.prepare()

        self.deck = Cards(
            ra=36, rb=8, rc=4, rd=4,
            ga=36, gb=8, gc=4, gd=4,
            ba=36, bb=8, bc=4, bd=4
        )

        self.order = list(self.players.keys())
        random.shuffle(self.order)

        self.status = -1
        self.turn = 0
        self.drawn = 0

    def finish(self):
        if self.status == 0:
            raise Exception("終了できません")

        for player in self.players.values():
            player.finish()

        self.status = 0
        self.deck = None
        self.order = None
        self.turn = None
        self.drawn = None

    def draw(self, sid, *, red=0, green=0, blue=0):
        if self.status == -1:
            if (red+green+blue) != 15:
                raise ValueError("無効な値です")
        elif self.status > 0:
            if (red+green+blue) != 1:
                raise ValueError("無効な値です")
        else:
            raise Exception("カードを引けません")

        if self.drawn != 0:
            raise Exception("カードを引けません")

        if red < 0 or green < 0 or blue < 0:
            raise ValueError("無効な値です")

        if sid != self.order[self.turn]:
            raise ValueError("このプレイヤーの番ではありません")

        drawn = self.deck.draw(red=red, green=green, blue=blue)
        self.players[sid].hand.add(**drawn)

        if self.status == -1:
            self.turn += 1
            if self.turn == len(self.order):
                self.turn = 0
                self.status = 1
        else:
            letter = drawn.keys()[0][1]
            if letter == "a":
                self.drawn = 100
            if letter in ("b", "c"):
                self.drawn = 500
            if letter == "d":
                self.drawn = 1000
            if letter == "e":
                self.drawn = 2000
