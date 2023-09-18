import sqlite3 as sq


with sq.connect('saper.db') as con:
    cur = con.cursor()  #Cursor


    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    sex INTEGER,
    old INTEGER,
    score INTEGER
    )""")
