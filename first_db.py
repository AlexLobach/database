import sqlite3

conn_1 = sqlite3.connect("db_first.db")
cursor_1 = conn_1.cursor()
cursor_1.execute(
    '''CREATE TABLE IF NOT EXISTS
        tab_1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        col_1 TEXT,
        col_2 TEXT,
        col_3 INTEGER
        )
    ''')

for i in range(3):
    input_id = int(input("Введите значение: "))
    cursor_1.execute("""INSERT INTO tab_1(col_1, col_2, col_3) VALUES(?,?,?)""", ('hello', 'world', input_id))

conn_1.commit()

cursor_1.execute('''SELECT col_3 FROM tab_1''')
for i in cursor_1.fetchall():
    print(i)
