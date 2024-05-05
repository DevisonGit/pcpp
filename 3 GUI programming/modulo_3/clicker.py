import tkinter as tk
from random import randint
from tkinter import messagebox


def list_number():
    numbers_clicker = []
    while len(numbers_clicker) < 25:
        rand = randint(1, 999)
        if rand not in numbers_clicker:
            numbers_clicker.append(rand)
    return numbers_clicker


def validate(event):
    global task_id
    number = event.__dict__.get('widget')['text']
    if number == list_number_sort[0]:
        event.__dict__.get('widget').config(state='disable')
        list_number_sort.pop(0)
    if len(list_number_sort) == 0:
        window.after_cancel(task_id)
        if messagebox.askquestion("", "You finish, do you want play again?") == "yes":
            start_game()
        else:
            window.destroy()


def create_buttons():
    count = 0
    for row in range(5):
        for column in range(5):
            button_name = tk.Button(window, text=list_numbers[count], width=8)
            button_name.bind("<Button-1>", validate)
            button_name.grid(row=row, column=column, sticky='nesw')
            count += 1


def start_counter():
    global counter
    global task_id
    counter += 1
    text.set(str(counter))
    task_id = label.after(1000, start_counter)


def callback(event):
    global first_click
    if not first_click:
        first_click = True
        start_counter()


def start_game():
    global first_click, task_id, counter, list_number_sort, window, label, text, list_numbers
    first_click = False
    window = tk.Tk()
    window.title("Clicker")
    window.geometry("320x160")
    window.resizable(width=False, height=False)
    task_id = "0"
    counter = 0
    text = tk.StringVar()
    list_numbers = list_number()
    create_buttons()
    text.set(str(counter))
    label = tk.Label(window, textvariable=text)
    label.grid(row=6, columnspan=6)
    list_number_sort = sorted(list_numbers)
    window.bind("<Button-1>", callback)
    window.mainloop()


start_game()
