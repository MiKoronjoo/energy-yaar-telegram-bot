import enum

import telepot


class State(enum.Enum):
    MAIN_MENU = 'MAIN_MENU'


from consts import *


class StateError(Exception):
    pass


class InputError(Exception):
    pass


class User:
    def __init__(self, user_id: int) -> None:
        self.id = user_id
        self.state = State.MAIN_MENU

    def __eq__(self, number: int) -> bool:
        return self.id == number

    def back(self) -> None:
        raise StateError('User in state "%s" can\'t back' % self.state.value)

    def say(self, message: str, bot: telepot.Bot) -> bool:
        raise InputError('"%s" is not a standard input' % message)
