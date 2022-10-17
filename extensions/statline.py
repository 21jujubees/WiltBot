import hikari
import lightbulb
import random
import pandas as pd
from nba_api.stats.endpoints import playergamelog, boxscoretraditionalv2

plugin = lightbulb.Plugin('Statline')


def getStatline():
    seasonsList = []
    COLUMNS = [
        "Game_ID", "GAME_DATE", "MATCHUP", "PTS", "AST", "REB", "WL", "FGM", "FGA", "FG_PCT", "FTM", "FTA", "FT_PCT", "MIN", "PF"
    ]
    x = 0

    while x < 14:
        seasonsList.append(str(1959 + x) + '-' + str(60 + x))
        x += 1

    randomSeason = random.choice(seasonsList)
    randomSeasonPhase = random.choice(['Regular Season', 'Playoffs'])

    game_log_list = playergamelog.PlayerGameLog(
        player_id=76375,
        season=randomSeason,
        season_type_all_star=randomSeasonPhase)

    gameLogsData = pd.concat(game_log_list.get_data_frames())
    randomGame = gameLogsData.sample()[COLUMNS]
    randomGame["LINK"] = "https://www.nba.com/game/" + gameLogsData["Game_ID"]

    pd.set_option('display.max_columns', None)
    return randomGame


def getURL(gameStatline):
    url = gameStatline.iloc[0]['LINK']
    return url

def getScore(gameStatline):
  gameID = gameStatline.iloc[0]['Game_ID']

  boxScore = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=gameID)
  boxScore = boxScore.get_data_frames()
  
  matchUp = gameStatline.iloc[0]['MATCHUP']
  
  wiltScore = 0
  enemyScore = 0
  
  if "@" in matchUp:
    wiltScore = boxScore[1].iloc[1]["PTS"]
    enemyScore = boxScore[1].iloc[0]["PTS"]
  else:
    wiltScore = boxScore[1].iloc[0]["PTS"]
    enemyScore = boxScore[1].iloc[1]["PTS"]
  
  finalScore = str(wiltScore) + " - " + str(enemyScore)
  return finalScore

@plugin.command
@lightbulb.command('statline', 'Get a random Wilt statline.')
@lightbulb.implements(lightbulb.SlashCommand)
async def statline(ctx: lightbulb.Context) -> None:
    gameStatline = getStatline()
    embed = hikari.Embed(
      title=gameStatline['MATCHUP'].iloc[0],
      description=getScore(gameStatline)
    )
    embed.add_field("DATE", gameStatline['GAME_DATE'].iloc[0])
    embed.set_thumbnail('76375.png')
    for column_name, item in gameStatline.items():
        if (column_name not in ['LINK', 'Game_ID', 'MATCHUP', 'GAME_DATE', 'WL']):
            embed.add_field(column_name,
                            item.to_string(index=False),
                            inline=True)
    embed.add_field("Source", "[nba.com](" + getURL(gameStatline) + ")")
    await ctx.respond(embed)


def load(bot):
    bot.add_plugin(plugin)
