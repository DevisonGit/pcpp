import sqlite3

delete = 'DELETE FROM tasks WHERE id = ?'

conn = sqlite3.connect('hello_v3.db')
cursor = conn.cursor()
cursor.execute(delete, (1, ))
conn.commit()
conn.close()
