import enum

import telepot


class State(enum.Enum):
    MAIN_MENU = 'MAIN_MENU'


from consts import *


class InputError(Exception):
    pass


class User:
    def __init__(self, user_id: int) -> None:
        self.id = user_id
        self.state = State.MAIN_MENU

    def __eq__(self, number: int) -> bool:
        return self.id == number

    def say(self, message: str, bot: telepot.Bot) -> bool:
        if message == '/start':
            self.state = State.MAIN_MENU
            return True

        raise InputError('"%s" is not a standard input' % message)
