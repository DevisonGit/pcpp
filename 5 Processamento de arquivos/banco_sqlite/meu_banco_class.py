import sqlite3

create_table = '''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);'''
insert_table = 'INSERT INTO tasks (name, priority) VALUES (?, ?)'


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('hello_v3.db')
        self.cursor = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.cursor.execute(create_table)

    def add_task(self):
        name = input('Enter task name: ')
        priority = int(input('Enter priority: '))
        self.cursor.execute(insert_table, (name, priority))
        self.conn.commit()


app = Todo()
app.add_task()
