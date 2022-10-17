import os
import hikari
import lightbulb
from webserver import keep_alive
import random

bot = lightbulb.BotApp(
    token=(os.getenv('token')),
    default_enabled_guilds=[1013200930415583263, 847259054999994398],
)

bot.load_extensions_from('./extensions')

def getTextList(fname):
    return open(fname).read().splitlines()

@bot.command
@lightbulb.command('weather', 'Get the latest forecast.')
@lightbulb.implements(lightbulb.SlashCommand)
async def weather(ctx):
    await ctx.respond("**spits** It's raining.")


@bot.command
@lightbulb.command('women', '20,000 women?!?')
@lightbulb.implements(lightbulb.SlashCommand)
async def women(ctx):
    await ctx.respond(
        "With all of you men out there who think that having a thousand different ladies is pretty cool, I have learned in my life I've found out that having one woman a thousand different times is much more satisfying."
    )


@bot.command
@lightbulb.command('russell',
                   'What does Wilt think of the late great Bill Russell?')
@lightbulb.implements(lightbulb.SlashCommand)
async def russell(ctx):
    await ctx.respond(
        "I guarantee you, if you could give me 10 points in all those seventh games against the Boston Celtics, instead of Bill Russell having 11 rings, I could've at least had nine or eight."
    )


@bot.command
@lightbulb.command('hundred', 'What does Wilt think of scoring 100 points?')
@lightbulb.implements(lightbulb.SlashCommand)
async def hundred(ctx):
    await ctx.respond(
      "Scoring 100 points is a lot, but I maybe could have scored 140 if they had played straight-up basketball.",
      attachment='img/100.jpg'
    )


@bot.command
@lightbulb.command('wilt',
                   'Hear an inspirational quote from Wilt Chamberlain!')
@lightbulb.implements(lightbulb.SlashCommand)
async def quotes(ctx):
    await ctx.respond(random.choice(getTextList('quotes.txt')))


@bot.command
@lightbulb.command('ego', 'Wilt and his ego.')
@lightbulb.implements(lightbulb.SlashCommand)
async def ego(ctx):
    await ctx.respond(
        "People say my ego is grand. I think it's in proportion to me.",
    attachment='img/2balls.jpg')


@bot.command
@lightbulb.command('election', 'Who would Wilt vote for?')
@lightbulb.implements(lightbulb.SlashCommand)
async def nixon(ctx):
    await ctx.respond(
        "I'd vote for Nixon a third time if I could.",
      attachment='img/nixon.png'
    )


@bot.command
@lightbulb.command('paternitytest', 'Is Wilt your father?')
@lightbulb.implements(lightbulb.SlashCommand)
async def paternity(ctx):
    await ctx.respond("Maybe. I should've worn a rubber.")


@bot.command
@lightbulb.command('contract', 'How much would Wilt make today?')
@lightbulb.implements(lightbulb.SlashCommand)
async def contract(ctx):
    await ctx.respond(
        "How much would I get paid today? Well, let's first talk about my owning part of the team."
    )


@bot.command
@lightbulb.command('top5', 'What would Wilt rank as his top five?')
@lightbulb.implements(lightbulb.SlashCommand)
async def top5(ctx):
    await ctx.respond(
        "Larry Bird, and uh let's see, Larry Bird, and I gotta go with Jerry, Oscar, and Elgin, and probably Jordan or Magic six, you gotta give me six. Can I have seven and put Sir Charles in there?"
    )


@bot.command
@lightbulb.command('jordan', 'What does Wilt think of Michael Jordan?')
@lightbulb.implements(lightbulb.SlashCommand)
async def jordan(ctx):
    await ctx.respond(
        "The difference between Jordan and me is that they had to change the rules for me so I couldn’t dominate. They changed the rules so that Jordan could.",
        attachment='img/jordan.jpg')


@bot.command
@lightbulb.command('rings', 'Rings, Erneh!')
@lightbulb.implements(lightbulb.SlashCommand)
async def rings(ctx):
    await ctx.respond(
        "I have a friend of mine who I talk to about once every week. You know what he says about Michael's six championships. He doesn't say anything about it. Because he has eleven."
    )
  
@bot.command
@lightbulb.command('trae', "Wilt's thoughts on Trae Young")
@lightbulb.implements(lightbulb.SlashCommand)
async def trae(ctx):
    await ctx.respond(
      attachment='vid/denzel.mp4'
    )

@bot.command
@lightbulb.command('porter', "Is Otto Porter Wilt's son?")
@lightbulb.implements(lightbulb.SlashCommand)
async def porter(ctx):
    await ctx.respond(
        "Otto who? You sure he's one of mine?"
    )

@bot.command
@lightbulb.command('mixtape', "Wilt has a mixtape?")
@lightbulb.implements(lightbulb.SlashCommand)
async def mixtape(ctx):
    await ctx.respond(
        "Check out my mixtape, follow me on Soundcloud: https://youtu.be/CCn323X3c_0"
    )

keep_alive()
bot.run()
