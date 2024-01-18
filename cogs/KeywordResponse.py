from cgitb import handler
from discord.ext import commands
from cogs.BaseCog import BaseCog
from utils.Action import Action, Bark

dog_name = "狗勾"


class KeywordResponse(BaseCog):
    def __init__(self, bot):
        super().__init__(bot)
        self.action = Action()
        self.bark = Bark()
        self.keyword_pre_handler = {
            "過來": self.action.come,
            "摸": self.action.touch,
            "蹭": self.action.nuzzle,
        }
        self.keyword_suf_handler = {
            f"{dog_name}": self.action.woof,
            "汪": self.action.more_woof,
            "握手": self.action.shake_hand,
            "坐下": self.action.sit,
            "趴下": self.action.lie_down,
            "抱": self.action.hug,
            "餓": self.action.give_food,
        }
        self.multiple_pre_keywords = {("搓", "揉"): self.action.rub}
        self.multiple_suf_keywords = {
            ("好累", "累了"): self.action.comfort,
            ("想睡", "睏"): self.action.lean,
            ("好乖", "很棒", "乖狗", "乖乖"): self.action.happy,
            ("不行", "不可以", "不乖", "壞"): self.action.sad,
        }

    def keywords_handler(self, keyword_dict, message):
        response_list = []
        for keyword, response_func in keyword_dict.items():
            if keyword in message.content:
                response_list.append(response_func())
        return response_list

    def mult_keywords_handler(self, keyword_dict, message):
        response_list = []
        for keywords, response_func in keyword_dict.items():
            if any(kw in message.content for kw in keywords):
                response_list.append(response_func())
        return response_list

    @commands.Cog.listener()
    async def on_message(self, message):
        responses = []

        if message.author == self.bot.user:
            return

        # prevent
        responses.extend(self.keywords_handler(self.keyword_pre_handler, message))
        responses.extend(
            self.mult_keywords_handler(self.multiple_pre_keywords, message)
        )

        # suffix
        responses.extend(self.keywords_handler(self.keyword_suf_handler, message))
        responses.extend(
            self.mult_keywords_handler(self.multiple_suf_keywords, message)
        )

        if dog_name in message.content and (
            "卡哇" in message.content or "可愛" in message.content
        ):
            responses.append(self.action.confuse())

        await message.channel.send("\n".join(responses))


async def setup(bot: commands.Bot):
    await bot.add_cog(KeywordResponse(bot))
