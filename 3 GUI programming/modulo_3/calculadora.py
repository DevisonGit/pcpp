import tkinter as tk
from tkinter import messagebox


def is_int_or_float(value):
    try:
        result = int(value)
    except ValueError:
        result = float(value)
    return result


def evaluate():
    value = 0
    a = None
    try:
        a = is_int_or_float(entry_1.get())
        b = is_int_or_float(entry_2.get())
        if operator.get() == 'add':
            value = a + b
        elif operator.get() == 'decrease':
            value = a - b
        elif operator.get() == 'multiply':
            value = a * b
        elif operator.get() == 'divide':
            value = a / b
        messagebox.showinfo("", f"value = {value}")
    except ValueError:
        messagebox.showerror("!", "Error: field contain invalid data")
        if a:
            entry_2.focus_set()
        else:
            entry_1.focus_set()
    except ZeroDivisionError:
        messagebox.showerror("!", "Error: Divide by zero")


window = tk.Tk()
window.title("Calculator")

operator = tk.StringVar()
operator.set("add")

entry_1 = tk.Entry(window)
entry_2 = tk.Entry(window)

radio_add = tk.Radiobutton(window, text="+", variable=operator, value='add')
radio_decrease = tk.Radiobutton(window, text='-', variable=operator, value='decrease')
radio_multiply = tk.Radiobutton(window, text='*', variable=operator, value='multiply')
radio_divide = tk.Radiobutton(window, text='/', variable=operator, value='divide')
button = tk.Button(window, text="Evaluate", command=evaluate)

entry_1.grid(column=0, row=1, rowspan=2)
entry_2.grid(column=2, row=1, rowspan=2)
radio_add.grid(column=1, row=0)
radio_decrease.grid(column=1, row=1)
radio_multiply.grid(column=1, row=2)
radio_divide.grid(column=1, row=3)
button.grid(column=1, row=4)

window.mainloop()
