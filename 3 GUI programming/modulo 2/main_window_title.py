import tkinter as tk


def click(*args):
    global count
    if count > 0:
        count -= 1
    window.title(str(count))


count = 10

window = tk.Tk()
window.title(str(count))
window.bind("<Button-1>", click)

window.mainloop()
