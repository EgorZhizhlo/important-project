from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from database import SQLite_db
from MARKUP import MarkUp


async def start(message: types.Message):
    await message.answer(f"🖐Здравствуйте, <b>{message.chat.first_name}</b>!\n"
                         f" <b>Market Vape Bot</b> - интернет-магазин никотиносодержащей продукции.\n"
                        "🗣Для перехода в меню введите команду: <b>/menu</b>",
                        reply_markup=MarkUp.start_keyboard)


async def help(message: types.Message):
    await message.answer("Для перехода в меню введите:\n"
                         "    <b>/menu</b>",
                        reply_markup=MarkUp.start_keyboard)


async def menu(message: types.Message):
    await message.answer("🤖 С помощью <b>Market Vape Bot</b> вы можете:\n"
                        " 🛒<u>Осуществить заказ</u>\n   Команда: <b>/order</b>\n"
                        " 👀<u>Узнать об актуальном ассортименте</u>\n   Команда: <b>/assortment</b>\n"
                        " 🏪<u>Узнать адреса официальных магазинов</u>\n   Команда: <b>/adress</b>\n"
                        " 📞<u>Связь с технической поддержкой</u>\n   Команда: <b>/phone</b>",
                        reply_markup=MarkUp.menu_keyboard)


async def order(message: types.Message):
    if not SQLite_db.user_reg(message.from_user.id):
        await message.reply("🤝Для осуществления заказа требуется зарегестрироваться в системе.\n"
                                                    "Команда: <b>/registration</b>",
                                                    reply_markup=MarkUp.reg_keyboard)
    else:
        await message.reply(f"<b>{message.chat.first_name}</b>, прежде чем оформить заказ, ознакомтесь с ассортиментом.\n"
                            "Ассортимент: <b>/assortment</b>\n"
                            "Оформить заказ: <b>/make_order</b>",
                            reply_markup=MarkUp.make_o_keyboard)


async def assortment(message: types.Message):
    await message.reply("✍Актуальный ассортимент магазина:\n"
                            "<b>Ссылка на ассортимент магазина</b>\n"
                        "Возврат в меню: <b>/menu</b>\n"
                        "Сделать заказ: <b>/make_order</b>",
                        reply_markup=MarkUp.m_keyboard)


async def adress_c(message: types.Message):
    await message.reply("🏪Адреса официальных магазинов:\n"
                            "<b>АДРЕС</b>\n"
                        "Возврат в меню: <b>/menu</b>",
                        reply_markup=MarkUp.start_keyboard)


async def phone(message: types.Message):
    await message.reply("📞Техническая поддержка:\n"
                            "<b>+7XXXXXXXXXX</b>\n"
                        "Возврат в меню: <b>/menu</b>",
                        reply_markup=MarkUp.start_keyboard)


def add_commands(dispatcher: Dispatcher):
    dispatcher.register_message_handler(assortment, commands="assortment")
    dispatcher.register_message_handler(help, commands="help")
    dispatcher.register_message_handler(adress_c, commands="adress")
    dispatcher.register_message_handler(phone, commands="phone")
    dispatcher.register_message_handler(start, commands="start")
    dispatcher.register_message_handler(menu, commands="menu")
    dispatcher.register_message_handler(order, commands="order")

