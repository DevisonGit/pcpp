import sqlite3

base_name = 'hello_v2.db'
create_table = '''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);'''
insert_table = 'INSERT INTO tasks (name, priority) VALUES (?, ?)'
tasks = [
    ('My first task', 1),
    ('My Second task', 2),
    ('My third task', 3)
]

conn = sqlite3.connect(base_name)
cursor = conn.cursor()
cursor.execute(create_table)
cursor.executemany(insert_table, tasks)
conn.commit()
conn.close()
