import sqlite3

conn = sqlite3.connect("db_fifth.db")
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS
        tab_1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        col_1 TEXT,
        col_2 TEXT        
        )
    ''')

# for i in range(3):
#     cursor.execute("""INSERT INTO tab_1(col_1, col_2) VALUES(?,?)""", ('hello', 'world'))

cursor.execute('''DELETE FROM tab_1 WHERE id = 2 ''')
conn.commit()
cursor.execute('''UPDATE tab_1 SET col_1= 'World', col_2 = 'Hello' WHERE id = 3 ''')
conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
data_ = cursor.fetchall()
#print(data_)

with open('data.txt', 'w') as file:
    for i in data_:
        for j in i:
            file.write(str(j) + ' ')
        file.write('\n')

