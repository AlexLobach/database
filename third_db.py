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

random_id = random.randint(0, 10)
for n in range(10):
    cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES(?,?)''', (random.randint(0, 10), random.randint(0, 10)))
conn.commit()
cursor.execute(f'''SELECT * FROM tab_1 WHERE id = {random_id} ''')

k = cursor.fetchall()
print(k)
values_ = [i for i in k[0]]
print(values_)

if values_[1] % 2 == 0 and values_[2] % 2 == 0:
    print(f'Удаление {random_id} строки.')
    cursor.execute(f'''DELETE FROM tab_1 WHERE id = {random_id}''')
    conn.commit()


else:
    print(f'Замена {random_id} строки на (2,2).')
    cursor.execute(f'''UPDATE tab_1 SET col_1 = 2, col_2 = 2 WHERE id = {random_id}''')
    conn.commit()

cursor.execute(f'''SELECT * FROM tab_1''')
print(cursor.fetchall())

