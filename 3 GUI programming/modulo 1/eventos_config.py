import tkinter as tk
from tkinter import messagebox


def click(event=None):
    if event is None:
        tk.messagebox.showinfo("Click!", "I love clicks")
    else:
        string = "x=" + str(event.x) + "y=" + str(event.y) + "num=" + str(event.num) + "type=" + str(event.type)
        tk.messagebox.showinfo("Click!", string)


window = tk.Tk()

label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)
label.pack()

button = tk.Button(window, text="Button", command=click)
button.config(command=lambda: None)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="red")
frame.bind("<Button-1>", click)
frame.pack()

window.mainloop()
