import enum

import telepot


class State(enum.Enum):
    MAIN_MENU = 'MAIN_MENU'
    ABOUT_US = 'ABOUT_US'
    Q1_SIZE = 'Q1_SIZE'
    Q2_USE = 'Q2_USE'
    Q3_P = 'Q3_P'
    Q4_ECG = 'Q4_ECG'
    RESULT = 'RESULT'


from consts import *


class InputError(Exception):
    pass


class User:
    def __init__(self, user_id: int) -> None:
        self.id = user_id
        self.state = State.MAIN_MENU
        self.size = 0
        self.ecg = 0
        self.p = 0

    def __eq__(self, number: int) -> bool:
        return self.id == number

    def get_result(self):
        c = 20
        return (self.size * c - self.ecg) * self.p

    def say(self, message: str, bot: telepot.Bot) -> bool:
        if message == '/start':
            self.state = State.MAIN_MENU
            return True

        if self.state == State.MAIN_MENU:
            if message == bl_start:
                self.state = State.Q1_SIZE
                return True
            elif message == bl_about_us:
                self.state = State.ABOUT_US
                return True

        elif self.state == State.ABOUT_US:
            if message == bl_calcule:
                self.state = State.Q1_SIZE
                return True
            elif message == bl_plan_review:
                self.state = State.MAIN_MENU
                return True

        elif self.state == State.Q1_SIZE:
            self.size = int(message)  # may raise ValueError
            self.state = State.Q2_USE
            return True

        elif self.state == State.Q2_USE:
            self.state = State.Q3_P
            return True

        elif self.state == State.Q3_P:
            if message == bl_t3000:
                self.p = 3000
            elif message == bl_t4000:
                self.p = 4000
            elif message == bl_t5600:
                self.p = 5600
            else:
                raise InputError('"%s" is not a standard input' % message)

            self.state = State.Q4_ECG
            bot.sendMessage(self.id, text_4 % message, reply_markup=no_rkb)
            return False

        elif self.state == State.Q4_ECG:
            self.ecg = int(message)  # may raise ValueError
            self.state = State.RESULT
            result = self.get_result()
            if result >= 0:
                bot.sendMessage(self.id, result_pos % result, reply_markup=rkb_result)
                return False
            else:
                bot.sendMessage(self.id, result_neg % -result, reply_markup=rkb_result)
                return False

        elif self.state == State.RESULT:
            if message == bl_recalcule:
                self.state = State.MAIN_MENU
                return True

        raise InputError('"%s" is not a standard input' % message)
