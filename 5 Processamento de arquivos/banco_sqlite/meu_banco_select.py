import sqlite3

select_table = 'SELECT * FROM tasks'

conn = sqlite3.connect('hello_v3.db')
cursor = conn.cursor()
result = cursor.execute(select_table)
for row in result:
    print(row)
conn.close()
