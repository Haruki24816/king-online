import random


class Cards(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, value in self.items():
            if len(key) != 2 or \
               key[0] not in ("r", "g", "b") or \
               key[1] not in ("a", "b", "c", "d", "e"):
                raise ValueError("無効な種類のカードが指定されています")
            if value < 1:
                raise ValueError("無効な枚数が指定されています")

    def add(self, cards):
        if not type(cards) == type(self):
            raise ValueError("Cardsクラスではありません")

        for kind, num in cards.items():
            if kind not in self:
                self[kind] = 0
            self[kind] += num

    def remove(self, cards):
        if not type(cards) == type(self):
            raise ValueError("Cardsクラスではありません")

        if not self.is_contained(cards):
            raise ValueError("指定されたカードは含まれていません")

        for kind, num in cards.items():
            self[kind] -= num
            if self[kind] == 0:
                self.pop(kind)

    def is_contained(self, cards):
        if not type(cards) == type(self):
            raise ValueError("Cardsクラスではありません")

        for kind, num in cards.items():
            if (kind not in self) or (self[kind] < num):
                return False

        return True

    def check_abcde_nums(self, a=0, b=0, c=0, d=0, e=0, bc=0):
        for num in (a, b, c, d, e, bc):
            if num < 0:
                raise ValueError("無効な値です")

        nums = self.count_abcde()

        if bc != 0 and b+c == 0:
            return nums["a"] >= a and (nums["b"]+nums["c"]) >= bc and nums["d"] >= d and nums["e"] >= e
        elif bc == 0 and b+c != 0:
            return nums["a"] >= a and nums["b"] >= b and nums["c"] >= c and nums["d"] >= d and nums["e"] >= e
        elif bc == 0 and b+c == 0:
            return nums["a"] >= a and nums["d"] >= d and nums["e"] >= e
        else:
            raise ValueError("無効な値です")

    def categorize_to_abcde(self):
        card_lists = {"a": [], "b": [], "c": [], "d": [], "e": []}

        for kind, num in self.items():
            for n in range(num):
                card_lists[kind[1]].append(kind)

        return card_lists

    def categorize_to_rgb(self):
        card_lists = {"r": [], "g": [], "b": []}

        for kind, num in self.items():
            for n in range(num):
                card_lists[kind[0]].append(kind)

        return card_lists

    def draw(self, *, r=0, g=0, b=0):
        card_list = []
        categorized_cards = self.categorize_to_rgb()
        drawn_cards = {}

        for letter, num in {"r": r, "g": g, "b": b}.items():
            card_list += random.sample(categorized_cards[letter], num)

        for kind in card_list:
            if kind not in drawn_cards:
                drawn_cards[kind] = 0
            drawn_cards[kind] += 1

        cards = Cards(drawn_cards)
        self.remove(cards)
        return cards

    def pay(self, *, a=0, b=0, c=0, d=0, e=0):
        card_list = []
        categorized_cards = self.categorize_to_abcde()
        paid_cards = {}

        for letter, num in {"a": a, "b": b, "c": c, "d": d, "e": e}.items():
            card_list += random.sample(categorized_cards[letter], num)

        for kind in card_list:
            if kind not in paid_cards:
                paid_cards[kind] = 0
            paid_cards[kind] += 1

        cards = Cards(paid_cards)
        self.remove(cards)
        return cards

    def count_abcde(self):
        nums = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0}

        for letter, card_list in self.categorize_to_abcde().items():
            nums[letter] = len(card_list)

        return nums

    def count_rgb(self):
        nums = {"r": 0, "g": 0, "b": 0}

        for letter, card_list in self.categorize_to_rgb().items():
            nums[letter] = len(card_list)

        return nums

    def min(self):
        if self.check_abcde_nums(a=1):
            return "a"
        if self.check_abcde_nums(bc=1):
            return "bc"
        if self.check_abcde_nums(d=1):
            return "d"
        if self.check_abcde_nums(e=1):
            return "e"

    def amount(self, king=False):
        card_values = {"a": 100, "b": 500, "c": 500, "d": 1000, "e": 2000}
        nums = self.count_abcde()
        amount = 0

        if king:
            card_values["c"] = -2000

        for letter in card_values:
            amount += card_values[letter] * nums[letter]

        return amount

    def payments(self, amount, cards):
        if not type(cards) == type(self):
            raise ValueError("Cardsクラスではありません")

        conditions = []
        min = self.min()

        def add_condition(*, a=0, bc=0, d=0, e=0):
            conditions.append({"a": a, "bc": bc, "d": d, "e": e})

        if amount == 100:
            if self.check_abcde_nums(a=1): add_condition(a=1)
            if min == "bc" and cards.check_abcde_nums(a=4):
                add_condition(bc=1)
            if min == "d" and (cards.check_abcde_nums(a=9) or cards.check_abcde_nums(a=4, bc=1)):
                add_condition(d=1)
            if min == "e" and ( \
               cards.check_abcde_nums(a=19) or \
               cards.check_abcde_nums(a=14, bc=1) or \
               cards.check_abcde_nums(a=9, bc=2) or \
               cards.check_abcde_nums(a=4, bc=3) or \
               cards.check_abcde_nums(a=9, d=1) or \
               cards.check_abcde_nums(a=4, bc=1, d=1)):
                add_condition(e=1)

        elif amount == 500:
            if self.check_abcde_nums(a=5):  add_condition(a=5)
            if self.check_abcde_nums(bc=1): add_condition(bc=1)
            if min == "d" and (cards.check_abcde_nums(a=5) or cards.check_abcde_nums(bc=1)):
                add_condition(d=1)
            if min == "e" and ( \
               cards.check_abcde_nums(a=10) or \
               cards.check_abcde_nums(a=5, bc=1) or \
               cards.check_abcde_nums(bc=2) or \
               cards.check_abcde_nums(d=1)):
                add_condition(e=1)

        elif amount == 1000:
            if self.check_abcde_nums(a=10):      add_condition(a=10)
            if self.check_abcde_nums(a=5, bc=1): add_condition(a=5, bc=1)
            if self.check_abcde_nums(bc=2):      add_condition(bc=2)
            if self.check_abcde_nums(d=1):       add_condition(d=1)
            if min == "e" and ( \
               cards.check_abcde_nums(a=10) or \
               cards.check_abcde_nums(a=5, bc=1) or \
               cards.check_abcde_nums(bc=2) or \
               cards.check_abcde_nums(d=1)):
                add_condition(e=1)

        elif amount == 2000:
            if self.check_abcde_nums(a=20):           add_condition(a=20)
            if self.check_abcde_nums(a=15, bc=1):     add_condition(a=15, bc=1)
            if self.check_abcde_nums(a=10, bc=2):     add_condition(a=10, bc=2)
            if self.check_abcde_nums(a=5, bc=3):      add_condition(a=5, bc=3)
            if self.check_abcde_nums(bc=4):           add_condition(bc=4)
            if self.check_abcde_nums(a=10, d=1):      add_condition(a=10, d=1)
            if self.check_abcde_nums(a=5, bc=1, d=1): add_condition(a=5, bc=1, d=1)
            if self.check_abcde_nums(bc=2, d=1):      add_condition(bc=2, d=1)
            if self.check_abcde_nums(d=2):            add_condition(d=2)
            if self.check_abcde_nums(e=1):            add_condition(e=1)

        else:
            raise ValueError("無効な値です")

        return conditions


class Player:

    def __init__(self):
        self.name = ""      #プレイヤー名
        self.status = 0     #プレイヤーのステータス 未準備：0 準備完了：1 ゲーム中：2
        self.hand = None    #手札 Cardsクラス
        self.debts = None   #借金 辞書
        self.paid = None    #支払った額
        self.changes = None #お釣り 辞書

    def prepare(self):
        self.status = 2
        self.hand = Cards()
        self.debts = {}
        self.paid = 0
        self.changes = {}

    def finish(self):
        self.status = 0
        self.hand = None
        self.debts = None
        self.paid = None
        self.changes = None

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

    def draw(self, sid, *, r=0, g=0, b=0):
        if self.status == -1:
            if (r+g+b) != 15:
                raise ValueError("無効な値です")
        elif self.status > 0:
            if (r+g+b) != 1:
                raise ValueError("無効な値です")
        else:
            raise Exception("カードを引けません")

        if self.drawn != 0:
            raise Exception("カードを引けません")

        for arg in (r, g, b):
            if arg < 0:
                raise ValueError("無効な値です")

        if sid != self.order[self.turn]:
            raise ValueError("このプレイヤーの番ではありません")

        drawn = self.deck.draw(r=r, g=g, b=b)
        self.players[sid].hand.add(drawn)

        if self.status == -1:
            self.turn += 1
            if self.turn == len(self.order):
                self.turn = 0
                self.status = 1
        else:
            letter = list(drawn.keys())[0][1]
            if letter == "a":
                self.drawn = 100
            if letter in ("b", "c"):
                self.drawn = 500
            if letter == "d":
                self.drawn = 1000
            if letter == "e":
                self.drawn = 2000
