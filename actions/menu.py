from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.menu import build_menu
from actions.close_remind import close_remind_button
from actions.postpone import postpone_30, postpone_1h
from actions.list_reminds import button_list_reminds
from utils.constants import LIST_ALL_FLAG, LIST_WEEK_FLAG, LIST_ALL_BUTTON, LIST_WEEK_BUTTON, LIST_30_BUTTON, LIST_10_BUTTON, DONE_BUTTON, POSTPONE_1H_BUTTON, POSTPONE_30M_BUTTON

def remind_button_menu(bot, chat_id):
    button_list = [
        InlineKeyboardButton("Postpone for 30 min 🕟", callback_data=POSTPONE_30M_BUTTON),
        InlineKeyboardButton("Postpone for 1 hour 🕕", callback_data=POSTPONE_1H_BUTTON),
        InlineKeyboardButton("Mark as done ✅", callback_data=DONE_BUTTON)
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    bot.send_message(chat_id=chat_id, text="What should I do with remind?🤔", reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    data = update.callback_query.data
    chat_id = query.message.chat.id
    if data == LIST_WEEK_BUTTON:
        button_list_reminds(bot, chat_id, LIST_WEEK_FLAG)
    elif data == LIST_10_BUTTON:
        button_list_reminds(bot, chat_id, '10')
    elif data == LIST_30_BUTTON:
        button_list_reminds(bot, chat_id, '30')
    elif data == LIST_ALL_BUTTON:
        button_list_reminds(bot, chat_id, LIST_ALL_FLAG)
    elif data == DONE_BUTTON:
        close_remind_button(bot, chat_id)
    elif data == POSTPONE_30M_BUTTON:
        postpone_30(bot, chat_id)
    elif data == POSTPONE_1H_BUTTON:
        postpone_1h(bot, chat_id)

    bot.answer_callback_query(update.callback_query.id)