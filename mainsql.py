import sqlite3 as sq


with sq.connect('saper.db') as con:
    cur = con.cursor()  #Cursor


    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    sex INTEGER,
    old INTEGER,
    score INTEGER
    )""")


