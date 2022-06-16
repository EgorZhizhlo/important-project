from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from database import SQLite_db
from MARKUP import MarkUp


class Registrate(StatesGroup):
    name = State()
    number = State()
    adress = State()


async def registrartion(message: types.Message):
    if not SQLite_db.user_reg(message.from_user.id):
        await Registrate.name.set()
        await message.reply("Введите ваше <b>Имя</b>.\n"
                        "Для выхода из меню регистрации введите:\n"
                        "    /stop",
                            reply_markup=MarkUp.stop_keyboard)
    else:
        await message.reply("Вы уже зарегестрированы в системе.\n"
                            "Для возврата в меню введите:\n"
                            "    /menu", reply_markup=MarkUp.start_keyboard)


async def name(message: types.Message, state: FSMContext):
    if str(message.text).lower() == "stop" or str(message.text).lower() == "/stop".lower() or \
        str(message.text).lower() == "отмена".lower() or str(message.text).lower() == "/отмена".lower():
            await message.answer("🗙Регистрация отменена.\n"
                                 "Для возвращения в меню введите:\n"
                                 "     /menu",
                                reply_markup=MarkUp.start_keyboard)
            await state.finish()
    elif str(message.text) != "" and str(message.text) != " " and len(str(message.text)) <= 15 and str(message.text) != ".":
        async with state.proxy() as date:
            date['user_id'] = message.from_user.id
            date['name'] = message.text
            await Registrate.next()
            await message.answer("📞Введите ваш <b>Номер</b>.\n"
                                 "Пример: <b>+79XXXXXXXXX</b> или <b>89XXXXXXXXX</b>.\n"
                                    "Для выхода из меню регистрации введите:\n"
                                    "    /stop",
                            reply_markup=MarkUp.stop_keyboard)
    else:
        await message.reply("Некоректный ввод данных☹")
        await Registrate.name.set()


async def number(message: types.Message, state: FSMContext):
    if str(message.text).lower() == "stop".lower() or str(message.text).lower() == "/stop".lower() or \
        str(message.text).lower() == "Отмена".lower() or str(message.text).lower() == "/Отмена".lower():
            await message.answer("🗙Регистрация отменена.\n"
                                 "Для возвращения в меню введите:\n"
                                 "     /menu",
                                reply_markup=MarkUp.start_keyboard)
            await state.finish()
    elif str(message.text) != "" and str(message.text) != " " and\
            (len(str(message.text)) >= 11 and len(str(message.text)) <= 12) and str(message.text) != ".":
        async with state.proxy() as date:
            date['number'] = message.text
            await message.answer("🏠Введите ваш <b>Адрес</b>(улица, строение, подъезд, квартира).\n"
                                 "Пример: <b>ул.XXXXX XX/X, подъезд XX, кв.XXXX</b>.\n"
                                 "Для выхода из меню регистрации введите:\n"
                                 "    /stop",
                            reply_markup=MarkUp.stop_keyboard)
            await Registrate.next()
    else:
        await message.reply("Некоректный ввод данных☹")
        await Registrate.number.set()


async def adress(message: types.Message, state: FSMContext):
    if str(message.text).lower() == "stop".lower() or str(message.text).lower() == "/stop".lower() or \
        str(message.text).lower() == "Отмена".lower() or str(message.text).lower() == "/Отмена".lower():
            await message.answer("🗙Регистрация отменена.\n"
                                 "Для возвращения в меню введите:\n"
                                 "     /menu",
                                reply_markup=MarkUp.start_keyboard)
            await state.finish()
    elif str(message.text) != "" and str(message.text) != " " and str(message.text) != ".":
        async with state.proxy() as date:
            date['adress'] = message.text
            await message.reply('✅Данные сохранены.\n'
                                "Возврат в меню: <b>/menu</b>.",
                                reply_markup=MarkUp.start_keyboard)
        await SQLite_db.sql_add_c(state)
        await state.finish()
    else:
        await message.reply("Некоректный ввод данных☹")
        await Registrate.adress.set()


def add_users(dispatcher: Dispatcher):
    dispatcher.register_message_handler(registrartion, commands=("registration"), state=None)
    dispatcher.register_message_handler(name, content_types=['text'], state=Registrate.name)
    dispatcher.register_message_handler(number, state=Registrate.number)
    dispatcher.register_message_handler(adress, state=Registrate.adress)