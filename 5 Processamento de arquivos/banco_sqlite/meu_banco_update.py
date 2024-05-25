import sqlite3


update = 'UPDATE tasks SET priority = ? WHERE id = ?'

conn = sqlite3.connect('hello_v3.db')
cursor = conn.cursor()
cursor.execute(update, (30, 1))
conn.commit()
conn.close()
