from telepot.namedtuple import KeyboardButton, ReplyKeyboardMarkup

from classes import State


def keyboard_maker(keyboard_labels):
    my_keyboard = []
    for row in keyboard_labels:
        keyboard_row = []
        for label in row:
            keyboard_row.append(KeyboardButton(text=label))

        my_keyboard.append(keyboard_row)

    return ReplyKeyboardMarkup(keyboard=my_keyboard, resize_keyboard=True)


# button labels
bl_back = '🔙'
bl_goto_main = '📋'

# error messages
err_bad_input = ''

# messages
msg_state = {
    State.MAIN_MENU.value: '🙂',
}

# reply keyboards
rkb_state = {
    State.MAIN_MENU.value: keyboard_maker([['', ''], ['']]),
}
