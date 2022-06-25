import hikari
import lightbulb
import os
import logging
import permafrost

log = logging.getLogger(__name__)

bot = lightbulb.BotApp(
    permafrost.__token__,
    default_enabled_guilds=(permafrost.DEFAULT_GUILD,),
    help_slash_command=False,
    intents=hikari.Intents.ALL
)

bot.load_extensions_from("./permafrost/extensions")

@bot.listen
async def on_starting(event: hikari.StartingEvent) -> None:
    print(f"Logging in as {bot.get_me().username} (Version: {permafrost.__version__})")

def run() -> None:
    if os.name != 'nt':
        import uvloop
        uvloop.install()
    bot.run()