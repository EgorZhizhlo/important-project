from aiogram.utils import executor
from Start.start_polling import dispatcher
from database import SQLite_db


async def on_startup(_):
    print('Bot start polling')
    SQLite_db.SQL_s()


from BOT_files import Commands, Registrate, Order

Commands.add_commands(dispatcher)
Registrate.add_users(dispatcher)
Order.add_order(dispatcher)

executor.start_polling(dispatcher, skip_updates=True, on_startup=on_startup)