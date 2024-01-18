from random import choice, randint


class Adj:
    happy_words = ["開心", "快樂", "高興", "愉快", "雀躍"]
    sad_words = ["難過", "悲傷", "失落", "低落", "沮喪", "委屈巴巴"]
    question_words = ["困惑", "疑惑", "不解", "茫然", "滿頭問號", "滿臉問號", "一臉問號"]
    crazy_words = ["瘋狂", "發瘋般"]

    def happy(self):
        return choice(self.happy_words)

    def sad(self):
        return choice(self.sad_words)

    def question(self):
        return choice(self.question_words)

    def crazy(self):
        return choice(self.crazy_words)


class Verb:
    wag_words = ["搖尾巴", "甩動尾巴", "瘋狂搖尾巴"]
    gaze_words = ["看著", "注視著", "望著", "凝視著"]
    sad_words = ["垂下頭", "垂下耳朵", "低著頭"]
    sit_words = ["坐好", "正坐", "坐下"]
    lie_words = ["趴好", "趴下", "趴在地上"]
    run_words = ["跑", "衝", "飛奔", "奔"]
    jump_words = ["跳起", "躍起", "彈起"]
    cozy_words = ["把身體重量放到你身上", "用鼻頭蹭了蹭你"]

    def random_reverse(self, words_list):
        if randint(0, 1):
            words_list.reverse()
        return "".join(words_list)

    def wag(self):
        return choice(self.wag_words)

    def gaze(self):
        return choice(self.gaze_words)

    def happy(self):
        words_list = [self.wag(), self.gaze() + "你"]
        return self.random_reverse(words_list)

    def sad(self):
        return choice(self.sad_words)

    def sit(self):
        return choice(self.sit_words)

    def lie(self):
        return choice(self.lie_words)

    def run(self):
        return choice(self.run_words)

    def jump(self):
        return choice(self.jump_words)

    def cozy(self):
        return choice(self.cozy_words)


class Bark:
    woof_words = ["汪", "汪汪"]

    def woof(self):
        return choice(self.woof_words)

    def more_woof(self):
        words = self.woof_words + ["汪汪汪"]
        return choice(words)


class Action:
    def __init__(self):
        self.adj = Adj()
        self.verb = Verb()
        self.bark = Bark()

    def come(self):
        sentences = [
            f"{self.verb.run()}過來",
            f"{self.adj.happy()}地{self.verb.run()}過來",
        ]
        return f"（{choice(sentences)}）"

    def touch(self):
        """摸"""
        sentences = [
            "🥰",
            f"（{self.verb.wag()}）",
            f"🥰（{self.verb.wag()}）",
            "（用頭蹭手）",
            "（把臉塞進你掌心）",
            "（用頭蹭蹭你一臉滿足）",
        ]
        return choice(sentences)

    def rub(self):
        """搓、揉"""
        woof = ["", f"{self.bark.woof()}！"]
        sentences = [
            "🥰",
            f"（{self.verb.wag()}）",
            f"（{self.adj.happy()}地{self.verb.wag()}）",
            f"🥰（{self.verb.wag()}）",
            f"（{self.adj.happy()}地{self.verb.gaze}你）",
            f"（邊{self.verb.wag()}，邊{self.adj.happy()}地{self.verb.gaze()}你）",
        ]
        return choice(woof) + choice(sentences)

    def nuzzle(self):
        """蹭"""
        sentences = [
            "將整個身體靠在你身上",
            "靜靜地靠著你",
            self.verb.wag(),
            self.adj.happy() + self.verb.wag(),
            self.adj.crazy() + self.verb.wag(),
        ]
        return f"（{choice(sentences)}）"

    def woof(self):
        return f"{self.bark.woof()}！"

    def more_woof(self):
        return f"{self.bark.more_woof()}！"

    def shake_hand(self):
        sentences = ["", f"並{self.verb.happy()}", f"一邊{self.verb.happy()}"]
        return "（把爪子放你手上" + choice(sentences) + "）"

    def sit(self):
        sentences = [
            f"乖巧地{self.verb.sit()}",
            f"邊{self.verb.sit()}邊{self.verb.happy()}",
        ]
        return f"（{choice(sentences)}）"

    def lie_down(self):
        """趴下"""
        sentences = [
            f"乖巧地{self.verb.lie()}",
            f"{self.verb.lie()}，抬眼{self.verb.gaze()}你",
            f"{self.verb.lie()}，{self.verb.wag()}",
        ]
        return f"（{choice(sentences)}）"

    def circle(self):
        """轉圈"""
        sentences = [
            "跟著你的手轉著圈",
            "開始追著自己的尾巴轉圈",
        ]
        return f"（{choice(sentences)}）"

    def hug(self):
        sentences1 = [
            "",
            f"{self.adj.happy()}",
        ]
        sentences2 = [
            "撲進你懷裡",
            "把臉塞到你懷中",
            "整隻撲到你身上",
        ]
        sentences3 = ["", f"，{self.verb.wag()}", f"一邊{self.verb.wag()}"]
        return "（" + choice(sentences1) + choice(sentences2) + choice(sentences3) + "）"

    def lick(self):
        """舔"""
        sentences = [
            "舔了你一下",
            f"{self.adj.crazy()}地舔你",
            f"{self.adj.happy()}地舔你",
            "不斷舔你的手",
        ]
        return f"（{choice(sentences)}）"

    def give_food(self):
        count = ["半", "一", "一", "一", "一"]
        items = ["塊骨頭", "支雞腿", "片鴨胸", "包洋芋片", "包薯條"]
        woof = ["", self.bark.woof()]
        return (
            f"（叼著{choice(count) + choice(items)}，高速{self.verb.run()}過來，放到你面前）"
            f"{choice(woof)}（一臉期待，{self.verb.wag()}{self.verb.gaze()}你）"
        )

    def comfort(self):
        """安慰"""
        sentences = [
            "靠在你身邊，",
            "發出嗚嗚的叫聲，",
        ]
        return f"（{choice(sentences) + choice(self.verb.cozy())}，看起來是想要安慰你）"

    def lean(self):
        """倚靠"""
        return f"（{choice(self.verb.cozy())}，乖巧地靠在你身邊）"

    def happy(self):
        sentences = [
            f"（{self.adj.happy()}地{self.verb.wag()}，並{self.verb.gaze()}你）",
            f"（{self.adj.happy()}地{self.verb.wag()}{self.verb.gaze()}你）",
            f"（{self.adj.happy()}邊{self.verb.wag()}，邊{self.verb.gaze()}你）",
        ]
        return f"（{choice(sentences)}）"

    def sad(self):
        sentences = [
            f"滿臉{self.adj.sad()}地{self.verb.gaze()}你",
            f"{self.adj.sad()}地{self.verb.sad()}",
            f"發出哼哼的{self.adj.sad()}叫聲",
        ]
        return f"（{choice(sentences)}）"

    def confuse(self):
        sentences = [
            f"{self.adj.question()}地{self.verb.gaze()}你",
            f"{self.adj.question()}地歪頭",
            f"{self.adj.question()}的樣子，一邊{self.verb.happy()}",
        ]
        return f"（{choice(sentences)}）"
