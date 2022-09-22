import sqlite3

conn = sqlite3.connect("db_homework25.db")
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS
        tab_text(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        col_1 TEXT        
        )
    ''')
cursor.execute(
    ''' CREATE TABLE IF NOT EXISTS 
    tab_number(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col_1 INTEGER
    )
    ''')


def distributor(list_: list):
    for value in list_:
        if type(value) == str:
            cursor.execute(f'''INSERT INTO tab_text(col_1) VALUES ('{value}')''')
            cursor.execute(f'''INSERT INTO tab_number(col_1) VALUES ({len(value)})''')
            conn.commit()
        elif type(value) == int:
            if value % 2 == 0:
                cursor.execute(f'''INSERT INTO tab_number(col_1) VALUES ({value})''')
                conn.commit()
            else:
                cursor.execute(f'''INSERT INTO tab_text(col_1) VALUES ('нечетное')''')
                conn.commit()


list_value = [1, 3, 4, 6, 'alex', 'relax', 'take', 12]
distributor(list_value)
cursor.execute('''SELECT * FROM tab_text''')
conn.commit()
tab_1 = cursor.fetchall()
cursor.execute('''SELECT * FROM tab_number''')
conn.commit()
tab_2 = cursor.fetchall()

if len(tab_2) > 5:
    cursor.execute('''DELETE FROM tab_text WHERE id = 1''')
    conn.commit()
    print("Удалена первая запись в таблице №1(текст)")
elif len(tab_2) < 5:
    cursor.execute('''UPDATE tab_text SET col_1 = 'Hello' WHERE id = 1''')
    conn.commit()
    print("Изменена первая запись в таблице №1(текст)")

cursor.execute('''SELECT * FROM tab_text''')
print(cursor.fetchall())
