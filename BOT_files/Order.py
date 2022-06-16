from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from database import SQLite_db
from MARKUP import MarkUp


from Start import start_polling


sp = [" "]


class Order(StatesGroup):
    Product = State()
    yes_or_no = State()


async def make_order(message: types.Message):
    if SQLite_db.user_reg(message.from_user.id):
        await Order.Product.set()
        await message.reply("<b>Введите название</b> товара или <b>опишите</b> его.\n"
                            "Для остановки оформления заказа введите:\n"
                            "    <b>/stop</b>.",
                            reply_markup=MarkUp.stop_keyboard)
    else:
        await message.reply("Вы еще не зарегистрированы в системе.\n"
                            "Для регистрации введи: <b>/registration</b>")


async def Product(message: types.Message, state: FSMContext):
    if str(message.text) == "/stop" or str(message.text).lower() == "stop" or \
        str(message.text).lower() == "отмена" or str(message.text).lower() == "/отмена":
        await message.answer("🗙Оформление заказа остановлено.\n"
                            "Для возвращения в меню введите:\n"
                            "     /menu",
                                reply_markup=MarkUp.start_keyboard)
        await state.finish()
        pass
    elif str(message.text) != "" and str(message.text) != " " and len(str(message.text)) <= 40 and str(message.text) != ".":
        async with state.proxy() as date:
            sp[0] = str(message.text)
        await message.answer('✅Ваш ответ сохранён.\n'
                             'Вы действительно желаете приобрести:\n'
                             f'<b>{message.text}</b>?\n'
                             'Введите: <b>/yes</b> или <b>/no</b>.', reply_markup=MarkUp.y_or_n_keyboard)
        await Order.next()
    else:
        await message.reply("Некоректный ввод данных☹")
        await Order.Product.set()


async def yes_or_no(message: types.Message, state: FSMContext):
    m = message.text
    if m == "/yes" or m == "yes" or m.lower() == "да" or m.lower() == "/да":
        lname = len(str(SQLite_db.get_user_name(message.from_user.id)))
        lnumber = len(str(SQLite_db.get_user_number(message.from_user.id)))
        ladress = len(str(SQLite_db.get_user_adress(message.from_user.id)))

        await start_polling.BOT.send_message("-1001658984157",
                                             f"Имя: {SQLite_db.get_user_name(message.from_user.id)[:lname - 3]}\n"
                                             f"Телефон: {SQLite_db.get_user_number(message.from_user.id)[:lnumber - 3]}\n"
                                             f"Адрес: {SQLite_db.get_user_adress(message.from_user.id)[:ladress - 3]}\n"
                                             f"ID: @{message.from_user.username}\n"
                                             f"Товар: {str(sp[0])}")
        await message.answer('✅Заказ сформирован \n'
                             'Ожидайте звонка оператора для подтверждения заказа.\n'
                             'Для возврата в меню введите:\n'
                             '    <b>/menu</b>',
                                reply_markup=MarkUp.start_keyboard)
        await state.finish()
    elif m.lower() == "/no" or m.lower() == "no" or m.lower() == "/нет" or m.lower() == "нет":
        await message.answer('🗙Заказ не сформирован \n'
                             'Для возврата в меню введите:\n'
                             '    <b>/menu</b>',
                                reply_markup=MarkUp.start_keyboard)
        await state.finish()
    else:
        await message.answer("Я вас не понял\n"
                             "Введите: <b>/yes</b> или <b>/no</b>.", reply_markup=MarkUp.y_or_n_keyboard)
        await Order.yes_or_no.set()


def add_order(dispatcher: Dispatcher):
    dispatcher.register_message_handler(make_order, commands=("make_order"), state=None)
    dispatcher.register_message_handler(Product, state=Order.Product)
    dispatcher.register_message_handler(yes_or_no, state=Order.yes_or_no)
