from discord.ext import commands
from cogs.BaseCog import BaseCog
from random import choice

dog_name = "狗勾"


def choice_word(words: list[str]) -> str:
    return choice(words)


class Adj:
    def __init__(self):
        pass

    def happy(self):
        words = ["開心", "快樂", "高興", "愉快", "雀躍"]
        return choice_word(words)

    def sad(self):
        words = ["難過", "悲傷", "失落", "低落", "沮喪", "委屈巴巴"]
        return choice_word(words)

    def question(self):
        words = ["困惑", "疑惑", "不解", "茫然", choice(["滿頭", "滿臉", "一臉"]) + "問號"]
        return choice_word(words)

    def crazy(self):
        words = ["瘋狂", "發瘋般"]
        return choice_word(words)


class Action:
    def __init__(self):
        self.wag_words: list[str] = ["搖尾巴", "甩動尾巴", "瘋狂搖尾巴"]
        self.gaze_words: list[str] = ["看著", "注視著", "望著", "凝視著"]

    def wag(self):
        return choice_word(self.wag_words)

    def gaze(self):
        return choice_word(self.gaze_words)

    def happy(self):
        words = self.wag_words + [i + "你" for i in self.gaze_words]
        return choice_word(words)

    def sad(self):
        words = ["垂下頭", "垂下耳朵", "低著頭"]
        return choice_word(words)

    def sit(self):
        words = ["坐好", "正坐", "坐下"]
        return choice_word(words)

    def lie(self):
        words = ["趴好", "趴下", "趴在地上"]
        return choice_word(words)

    def run(self):
        words = ["跑", "衝", "飛奔", "奔"]
        return choice_word(words)

    def jump(self):
        words = ["跳起", "躍起", "彈起"]
        return choice_word(words)


class Bark(Action):
    def __init__(self):
        self.woof_words: list[str] = ["汪", "汪汪"]

    def woof(self):
        return choice_word(self.woof_words)

    def more_woof(self):
        words = self.woof_words
        words.append("汪汪汪")
        return choice_word(words)


class KeywordResponse(BaseCog):
    @commands.Cog.listener()
    async def on_message(self, message):
        adj = Adj()
        action = Action()
        bark = Bark()

        if message.author == self.bot.user:
            return

        if "過來" in message.content:
            sentences = [f"{action.run()}過來", f"{adj.happy()}地{action.run()}過來"]
            await message.channel.send(f"（{choice(sentences)}）")

        if "摸" in message.content:
            sentences = [
                "🥰",
                f"（{action.wag()}）",
                f"🥰（{action.wag()}）",
                "（用頭蹭手）",
                "（把臉塞進你掌心）",
                "（用頭蹭蹭你一臉滿足）",
            ]
            await message.channel.send(choice(sentences))

        if "搓" in message.content or "揉" in message.content:
            woof = ["", bark.woof()]
            sentences = [
                "🥰",
                f"（{action.wag()}）",
                f"（{adj.happy()}地{action.wag()}）",
                f"🥰（{action.wag()}）",
                f"{adj.happy()}地{action.gaze}你",
                f"邊{action.wag()}，邊{adj.happy()}地{action.gaze}你",
            ]
            await message.channel.send(choice(woof) + choice(sentences))

        if "蹭" in message.content:
            sentences = [
                "將整個身體靠在你身上",
                "靜靜地靠著你",
                action.wag(),
                adj.happy() + action.wag(),
                adj.crazy() + action.wag(),
            ]
            await message.channel.send(f"（{choice(sentences)}）")

        if dog_name in message.content:
            await message.channel.send(f"{bark.woof()}！")

        if "汪" in message.content:
            await message.channel.send(f"{bark.more_woof()}！")

        if "握手" in message.content:
            sentences = ["", f"並{action.happy()}", f"一邊{action.happy()}"]
            await message.channel.send("（把爪子放你手上" + choice(sentences) + "）")

        if "坐下" in message.content:
            sentences = [
                f"乖巧地{action.sit()}",
                f"邊{action.sit()}邊{action.happy()}",
            ]
            await message.channel.send(f"（{choice(sentences)}）")

        if "趴下" in message.content:
            sentences = [
                f"乖巧地{action.lie()}",
                f"{action.lie()}，抬眼{action.gaze()}你",
                f"{action.lie()}，{action.wag()}",
            ]
            await message.channel.send(f"（{choice(sentences)}）")

        if "轉圈" in message.content:
            sentences = [
                "跟著你的手轉著圈",
                "開始追著自己的尾巴轉圈",
            ]
            await message.channel.send(f"（{choice(sentences)}）")

        if "抱" in message.content:
            sentences1 = [
                "",
                f"{adj.happy()}",
            ]
            sentences2 = [
                "撲進你懷裡",
                "把臉塞到你懷中",
                "整隻撲到你身上",
            ]
            sentences3 = ["", f"，{action.wag()}", f"一邊{action.wag()}"]
            await message.channel.send(
                "（" + choice(sentences1) + choice(sentences2) + choice(sentences3) + "）"
            )

        if "舔" in message.content:
            sentences = [
                "舔了你一下",
                f"{adj.crazy()}地舔你",
                f"{adj.happy()}地舔你",
                "不斷舔你的手",
            ]
            await message.channel.send(f"（{choice(sentences)}）")

        if "餓" in message.content:
            count = ["半", "一", "一", "一", "一"]
            items = ["塊骨頭", "支雞腿", "片鴨胸", "包洋芋片", "包薯條"]
            woof = ["", bark.woof()]
            await message.channel.send(
                f"（叼著{choice(count) + choice(items)}，高速{action.run()}過來，放到你面前）"
            )
            await message.channel.send(
                f"{choice(woof)}（一臉期待，{action.wag()}{action.gaze()}你）"
            )

        if "好累" in message.content or "累了" in message.content:
            sentences1 = [
                "靠在你身邊，",
                "發出嗚嗚的叫聲，",
            ]
            sentences2 = [
                "把身體重量放到你身上",
                "用鼻頭蹭了蹭你",
            ]
            await message.channel.send(
                f"（{choice(sentences1) + choice(sentences2)}，看起來是想要安慰你）"
            )

        if "想睡" in message.content or "睏" in message.content:
            sentences1 = ["", bark.woof()]
            sentences2 = [
                "把身體重量放到你身上",
                "用鼻頭蹭了蹭你",
            ]
            await message.channel.send(
                f"（{choice(sentences1) + choice(sentences2)}，乖巧地靠在你身邊）"
            )

        if "好乖" in message.content or "很棒" in message.content or "乖" in message.content:
            sentences = [
                f"（{adj.happy()}地{action.wag()}，並{action.gaze()}你）",
                f"（{adj.happy()}地{action.wag()}{action.gaze()}你）",
                f"（{adj.happy()}邊{action.wag()}，邊{action.gaze()}你）",
            ]
            await message.channel.send(choice(sentences))

        if (
            "不行" in message.content
            or "不可以" in message.content
            or "不乖" in message.content
            or "壞" in message.content
        ):
            sentences = [
                f"滿臉{adj.sad()}地{action.gaze()}你",
                f"{adj.sad()}地{action.sad()}",
                f"發出哼哼的{adj.sad()}叫聲",
            ]
            await message.channel.send(f"（{choice(sentences)}）")

        if dog_name in message.content and (
            "卡哇" in message.content or "可愛" in message.content
        ):
            sentences = [
                f"{adj.question()}地{action.gaze()}你",
                f"{adj.question()}地歪頭",
                f"{adj.question()}的樣子，一邊{action.happy()}",
            ]
            await message.channel.send(f"（{choice(sentences)}）")


async def setup(bot: commands.Bot):
    await bot.add_cog(KeywordResponse(bot))
