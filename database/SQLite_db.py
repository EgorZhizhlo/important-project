import sqlite3 as sq


def SQL_s():
    global base, cur
    base = sq.connect("C:/Users/ToRiMO/PycharmProjects/t_b/database/users_date_db.db")
    cur = base.cursor()
    if base:
        print("Data base connected was OK!")
    base.execute('CREATE TABLE IF NOT EXISTS user_d(user_id INTEGER, user_n TEXT, user_num TEXT, user_a TEXT)')
    base.commit()


async def sql_add_c(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO user_d VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()


def user_reg(user_id):
    with base:
        result = cur.execute("SELECT * FROM user_d WHERE user_id = ?", (user_id,)).fetchall()
        return bool(len(result))


def get_user_name(user_id):
    with base:
        result = cur.execute("SELECT user_n FROM user_d WHERE user_id = ?", (user_id,)).fetchall()
        return str(result[0])[2:]


def get_user_number(user_id):
    with base:
        result = cur.execute("SELECT user_num FROM user_d WHERE user_id = ?", (user_id,)).fetchall()
        return str(result[0])[2:]


def get_user_adress(user_id):
    with base:
        result = cur.execute("SELECT user_a FROM user_d WHERE user_id = ?", (user_id,)).fetchall()
        return str(result[0])[2:]