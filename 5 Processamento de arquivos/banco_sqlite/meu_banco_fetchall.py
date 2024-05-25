import sqlite3

select_table = 'SELECT * FROM tasks'

conn = sqlite3.connect('hello_v3.db')
cursor = conn.cursor()
cursor.execute(select_table)
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
