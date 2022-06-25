import hikari
import lightbulb
import logging
from permafrost import random_color

log = logging.getLogger(__name__)

plugin = lightbulb.Plugin("Ping")

@plugin.command
@lightbulb.command("ping", "Checks the bot's latency.")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def ping_cmd(ctx: lightbulb.Context) -> None:
    latency = "{:.0f}".format(ctx.bot.heartbeat_latency * 1000)
    checkmark = ctx.bot.d.emojis["pf_checkmark"]
    embed = hikari.Embed(
        title=f"{checkmark} Pong!",
        description=f"Latency: {latency}ms",
        color=random_color()
    )
    await ctx.respond(embed=embed)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)

