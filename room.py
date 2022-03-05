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
        if type(cards) != type(self):
            raise ValueError("Cardsクラスではありません")

        for kind, num in cards.items():
            if kind not in self:
                self[kind] = 0
            self[kind] += num

    def remove(self, cards):
        if type(cards) != type(self):
            raise ValueError("Cardsクラスではありません")

        if not self.is_contained(cards):
            raise ValueError("指定されたカードは含まれていません")

        for kind, num in cards.items():
            self[kind] -= num
            if self[kind] == 0:
                self.pop(kind)

    def is_contained(self, cards):
        if type(cards) != type(self):
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

    def can_pay(self, amount, cards, a=0, bc=0, d=0, e=0):
        if type(cards) != type(self):
            raise ValueError("Cardsクラスではありません")

        nums = {"a": a, "bc": b+c, "d": d, "e": e}

        if amount == 100:
            condition = {}
            if self.min() == 100:
                condition = {"a": 1, "bc": 0, "d": 0, "e": 0}
            if self.min() == 500 and \
               cards.check_abcde_nums(a=4):
                condition = {"a": 0, "bc": 1, "d": 0, "e": 0}
            if self.min() == 1000 and (\
               cards.check_abcde_nums(a=9) or \
               cards.check_abcde_nums(a=4, bc=1)):
                condition = {"a": 0, "bc": 0, "d": 1, "e": 0}
            if self.min() == 2000 and (\
               cards.check_abcde_nums(a=19) or \
               cards.check_abcde_nums(a=14, bc=1) or \
               cards.check_abcde_nums(a=9, bc=2) or \
               cards.check_abcde_nums(a=4, bc=3) or \
               cards.check_abcde_nums(a=9, d=1) or \
               cards.check_abcde_nums(a=4, bc=1, d=1)):
                condition = {"a": 0, "bc": 0, "d": 0, "e": 1}
            if nums != condition:
                return False

        elif amount in (500, 1000, 1500, 2000):
            if not self.check_abcde_nums(**nums):
                return False
            payment_amount = 0
            for letter, value in {"a": 100, "bc": 500, "d": 1000, "e": 2000}.items():
                payment_amount += value * nums[letter]
            if (payment_amount%500) != 0:
                return False
            if payment_amount > amount:
                return False

        else:
            raise ValueError("無効な値です")

        return True


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
        self.status = 0   #部屋のステータス 募集中：0 準備中：-1 返済待ち：-2 ゲーム終了時：-3 ゲーム中：1以上（周数）
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
            self.drawn = drawn.amount()

    def pay(self, sid, *, a=0, b=0, c=0, d=0, e=0):
        player = self.players[sid]
        turn_player = self.players[self.order[self.turn]]

        if self.status < 1:
            raise Exception("支払いできません")

        if self.drawn == 0:
            raise Exception("支払いできません")

        if sid == self.order[self.turn]:
            raise ValueError("順番のプレイヤーです")

        if player.paid == self.drawn:
            raise ValueError("支払い済みです")

        for num in (a, b, c, d, e):
            if num < 0:
                raise ValueError("無効な値です")

        if not player.hand.can_pay(self.drawn-player.paid, turn_player.hand, a=a, bc=b+c, d=d, e=e):
            raise ValueError("無効な値です")

        paid = player.hand.pay(a=a, b=b, c=c, d=d, e=e)
        turn_player.hand.add(paid)

        if self.drawn == 100 and paid.amount() != 100:
            turn_player.changes[sid] = paid.amount() - 100
            player.paid = 100
        else:
            player.paid += paid.amount()

        try:
            self.next_turn()
        except Exception:
            pass

    def next_turn(self):
        if self.status < 1:
            raise Exception("ターンを送ることができません")

        if self.drawn == 0:
            raise Exception("ターンを送ることができません")

        turn_player = self.players[self.order[self.turn]]

        for player in self.players.values():
            if player == turn_player:
                continue
            if player.paid != self.drawn:
                raise Exception("支払いを完了していないプレイヤーがいます")

        if len(turn_player.changes) != 0:
            raise Exception("お釣りの返却が済んでいません")

        self.turn += 1

        if self.turn == len(self.order):
            self.turn = 0
            self.status += 1
            self.drawn = 0
            for player in self.players.values():
                player.paid = 0

    def give_change(self, sid, opponent_sid, *, a=0, b=0, c=0, d=0, e=0):
        player = self.players[sid]
        opponent_player = self.players[opponent_sid]

        if self.status < 1:
            raise Exception("お釣りを渡せません")

        if self.drawn == 0:
            raise Exception("お釣りを渡せません")

        if sid != self.order[self.turn]:
            raise ValueError("順番のプレイヤーではありません")

        if opponent_sid not in player.changes:
            raise ValueError("お釣りは要りません")

        for num in (a, b, c, d, e):
            if num < 0:
                raise ValueError("無効な値です")

        amount = 0

        for letter, value in {"a": 100, "bc": 500, "d": 1000, "e": 2000}.items():
            amount += value * {"a": a, "bc": b+c, "d": d, "e": e}[letter]

        if amount != player.changes[opponent_sid]:
            raise ValueError("金額が一致しません")

        change = player.hand.pay(a=a, b=b, c=c, d=d, e=e)
        opponent_player.hand.add(change)
        player.changes.pop(opponent_sid)

        try:
            self.next_turn()
        except Exception:
            pass

    def borrow(self, sid, amount):
        player = self.players[sid]
        turn_player = self.players[self.order[self.turn]]

        if self.status < 1:
            raise Exception("借金できません")

        if self.drawn == 0:
            raise Exception("借金できません")

        if sid == self.order[self.turn]:
            raise ValueError("順番のプレイヤーです")

        if amount not in (500, 1000, 1500, 2000):
            raise ValueError("無効な値です")

        if (self.drawn-player.paid) < amount:
            raise ValueError("金額が多すぎます")

        player.debt(self.order[self.turn], amount)
        turn_player.debt(sid, (amount*-1))
        player.paid += amount

        try:
            self.next_turn()
        except Exception:
            pass

    def repay(self, sid, opponent_sid, *, a=0, b=0, c=0, d=0, e=0):
        player = self.players[sid]
        opponent_player = self.players[opponent_sid]

        if not (self.status > 0 or self.status == -3):
            raise Exception("返済できません")

        if opponent_sid not in player.debts:
            raise ValueError("借金がありません")

        for num in (a, b, c, d, e):
            if num < 0:
                raise ValueError("無効な値です")

        amount = 0

        for letter, value in {"a": 100, "bc": 500, "d": 1000, "e": 2000}.items():
            amount += value * {"a": a, "bc": b+c, "d": d, "e": e}[letter]

        if amount > player.debts[opponent_sid]:
            raise ValueError("金額が多すぎます")

        if (amount%500) != 0:
            raise ValueError("無効な値です")

        paid = player.hand.pay(a=a, b=b, c=c, d=d, e=e)
        opponent_player.hand.add(paid)
        player.debt(opponent_sid, (amount*-1))
        opponent_player.debt(sid, amount)
