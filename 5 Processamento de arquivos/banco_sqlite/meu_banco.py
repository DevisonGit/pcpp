import sqlite3

conn = sqlite3.connect('hello.db')
cursor = conn.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')

cursor.execute('INSERT INTO tasks (name, priority) VALUES (?, ?);', ('My first task', 1))
cursor.execute('INSERT INTO tasks (name, priority) VALUES (?, ?);', ('Second task', 2))
conn.commit()
conn.close()
