from aiogram import types


start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_buttons = [types.KeyboardButton(text="/menu")]
start_keyboard.add(*start_buttons)


menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
menu_buttons = [
        types.KeyboardButton(text="/order"),
        types.KeyboardButton(text="/assortment"),
        types.KeyboardButton(text="/adress"),
        types.KeyboardButton(text="/phone")
    ]
menu_keyboard.add(*menu_buttons)


reg_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
reg_buttons = [types.KeyboardButton(text="/registration")]
reg_keyboard.add(*reg_buttons)


order_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
order_buttons = [types.KeyboardButton(text="/order")]
order_keyboard.add(*order_buttons)


make_o_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
make_o_buttons = [types.KeyboardButton(text="/assortment"),
                  types.KeyboardButton(text="/make_order")]
make_o_keyboard.add(*make_o_buttons)


m_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
m_buttons = [types.KeyboardButton(text="/menu"),
             types.KeyboardButton(text="/make_order")]
m_keyboard.add(*m_buttons)

stop_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
stop_buttons = [types.KeyboardButton(text="/stop")]
stop_keyboard.add(*stop_buttons)


y_or_n_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
y_or_n_buttons = [types.KeyboardButton(text="/yes"),
             types.KeyboardButton(text="/no")]
y_or_n_keyboard.add(*y_or_n_buttons)