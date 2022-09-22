import sqlite3

conn = sqlite3.connect('db_fourth.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS 
    tab_1(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col_1 INTEGER
    )'''
)
#conn.commit()

class DB:
    def edit_db(self, arg_1=None, arg_2=None, arg_3=None):
        if arg_1 is not None and arg_2 is None and arg_3 is None:
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES (3)''')
            conn.commit()
        elif arg_1 is not None and arg_2 is not None and arg_3 is None:
            if type(arg_2) == int:
                cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
                conn.commit()
        elif arg_1 is not None and arg_2 is not None and type(arg_3) == int:
            cursor.execute('''UPDATE tab_1 SET col_1 = 77 WHERE id = 3''')
            conn.commit()


database_ = DB()
database_.edit_db('hello',2,3)
cursor.execute('''SELECT * FROM tab_1''')
conn.commit()
print(cursor.fetchall())
