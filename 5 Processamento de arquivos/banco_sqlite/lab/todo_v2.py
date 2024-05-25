import sqlite3

create_table = '''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);'''
select_task_by_name = 'SELECT * FROM tasks WHERE name = (?)'
select_all = 'SELECT * FROM tasks'
insert_table = 'INSERT INTO  tasks (name, priority) VALUES (?, ?)'
select_task_by_id = 'SELECT * FROM tasks WHERE id = (?)'
update_priority = 'UPDATE tasks SET priority = ?  WHERE id = ?'
delete_by_id = 'DELETE FROM tasks WHERE id = ?'


class Todo:
    def __init__(self, base_name):
        self.conn = sqlite3.connect(base_name)
        self.cursor = self.conn.cursor()
        self.create_table()
        self.options = {
            '1': self.show_tasks,
            '2': self.add_task,
            '3': self.change_priority,
            '4': self.delete_task,
            '5': self.exit
        }

    def create_table(self):
        self.cursor.execute(create_table)

    def add_task(self):
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

    def show_tasks(self):
        rows = self.cursor.execute(select_all)
        for row in rows:
            print(*row)

    def find_task_id(self, id_task):
        self.cursor.execute(select_task_by_id, (id_task,))
        return self.cursor.fetchone()

    def change_priority(self):
        try:
            id_task = input('which task should change the priority? ')
            if self.find_task_id(id_task) is not None:
                new_priority = int(input('what is the new priority? '))
                if new_priority > 0:
                    self.cursor.execute(update_priority, (new_priority, id_task))
                else:
                    raise ValueError
            else:
                print('Task with this id not found')
        except ValueError:
            print('Value invalid for new priority')

    def delete_task(self):
        id_task = input('Which task do you want to delete? ')
        if self.find_task_id(id_task) is not None:
            self.cursor.execute(delete_by_id, (id_task, ))
        else:
            print('Task with this id not found')

    @staticmethod
    def exit():
        print('bye')
        exit(0)

    def show_menu(self):
        print()
        print('1. Show Tasks\n'
              '2. Add Task\n'
              '3. Change Task\n'
              '4. Delete Task\n'
              '5. Exit')
        option = input('Choice a option: ')
        print()
        if option in self.options:
            self.options.get(option)()
        else:
            print('Choice invalid')


table = Todo('todo.db')
while True:
    table.show_menu()
