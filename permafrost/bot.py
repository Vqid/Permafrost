import hikari
import lightbulb
import os
import logging
import permafrost
from permafrost import Database

log = logging.getLogger(__name__)

bot = lightbulb.BotApp(
    permafrost.__token__,
    default_enabled_guilds=(permafrost.DEFAULT_GUILD,),
    prefix=permafrost.PREFIX,
    help_slash_command=False,
    intents=hikari.Intents.ALL
)

bot.load_extensions_from("./permafrost/extensions/info")

@bot.listen(hikari.StartingEvent)
async def on_starting(event: hikari.StartingEvent) -> None:
    log.info(f"❄️  Logging in as {permafrost.__username__}...")
    emojis = await bot.rest.fetch_guild_emojis(permafrost.DEFAULT_GUILD)
    bot.d.emojis = {e.name: e for e in emojis}
    bot.d.db = Database(permafrost._dynamic, permafrost._static)
    await bot.d.db.connect()
    
@bot.listen(hikari.StartedEvent)
async def on_ready(event: hikari.StartedEvent) -> None:
    log.info(f"❄️  Ready!")

def run() -> None:
    if os.name != 'nt':
        import uvloop
        uvloop.install()
    bot.run()