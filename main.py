import time

import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

from config import *
from classes import *

users = []  # Should save in database


def handle_chat(msg: dict) -> None:
    global users
    content_type, chat_type, chat_id = telepot.glance(msg)
    if chat_type == u'private':
        if content_type == 'text':
            if chat_id not in users:
                this_user = User(chat_id)
                users.append(this_user)
            else:
                this_user = users[users.index(chat_id)]

            try:
                send_message = this_user.say(msg['text'], bot)

                if send_message:
                    bot.sendMessage(chat_id, msg_state[this_user.state.value],
                                    reply_markup=rkb_state[this_user.state.value])

            except InputError:
                bot.sendMessage(chat_id, err_bad_input)


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle_chat).run_as_thread()

while True:
    time.sleep(30)
