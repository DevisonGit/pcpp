import sqlite3

create_table = '''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);'''
select_task_by_name = 'SELECT * FROM tasks WHERE name = (?)'
select_all = 'SELECT * FROM tasks'
insert_table = 'INSERT INTO  tasks (name, priority) VALUES (?, ?)'


class Todo:
    def __init__(self, base_name):
        self.conn = sqlite3.connect(base_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(create_table)

    def insert_task(self):
        try:
            name = input('Enter task name: ')
            priority = int(input('Enter priority: '))
            if name != '' and self.find_task(name) is None and priority > 1:
                self.cursor.execute(insert_table, (name, priority))
                self.conn.commit()
            else:
                print('Task name is null or already exists')
        except ValueError:
            print('Priority must be an integer number')

    def find_task(self, name):
        self.cursor.execute(select_task_by_name, (name, ))
        return self.cursor.fetchone()

    def show_task(self):
        rows = self.cursor.execute(select_all)
        for row in rows:
            print(*row)


table = Todo('todo.db')
table.insert_task()
table.show_task()
