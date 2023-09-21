import sqlite3 as sq

cars = [
    ('Audi', 52642),
    ('Merseces', 57127),
    ('skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)
]


with sq.connect('cars.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS cars(
                car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT,
                price INTEGER)''')

    #for car in cars:
    #    cur.execute("INSERT INTO cars VALUES(Null, ?, ?)", car)

    cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)