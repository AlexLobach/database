import sqlite3
import random

conn = sqlite3.connect('db_second.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS 
    tab_1(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col_1 INTEGER,
    col_2 INTEGER)'''
)

for n in range(5):
    cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES(?,?)''', (random.randint(0, 9), random.randint(0, 9)))

cursor.execute('''SELECT col_1, col_2 FROM tab_1''')
conn.commit()
k = cursor.fetchall()

sum_ = sum([sum(i) for i in k])


if (sum_ / (len(k) * 2)) > len(k):
    print("Удаляем 4 запись в базе данных.")
    cursor.execute('''DELETE FROM tab_1 WHERE id = 4''')
    conn.commit()
    cursor.execute('''SELECT * FROM tab_1''')
    conn.commit()
    print(cursor.fetchall())
else:
    print("Все хорошо, ничего не удаляем.")


