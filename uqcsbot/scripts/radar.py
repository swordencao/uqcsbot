from uqcsbot import command_handler, bot
from uqcsbot.command_handler import Command
from time import time


@command_handler.on("radar")
def handle_radar(command: Command):
    time_in_ms = int(round(time() * 1000))
    bot.post_message(command.channel, f'https://bom.lambda.tools/?location=brisbane&_cache={time_in_ms}')