import sqlite3

select_table = 'SELECT * FROM tasks'

conn = sqlite3.connect('hello_v3.db')
cursor = conn.cursor()
cursor.execute(select_table)
next_row = cursor.fetchone()
print(next_row)
next_row = cursor.fetchone()
print(next_row)
