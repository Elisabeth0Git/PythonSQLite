import sqlite3 as sq


with sq.connect('saper.db') as con:
    cur = con.cursor()  #Cursor


    cur.execute('SELECT * FROM users')
    result = cur.fetchall()
    print(result)