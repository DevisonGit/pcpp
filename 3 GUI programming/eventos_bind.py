import tkinter as tk
from tkinter import messagebox


def click(env=None):
    tk.messagebox.showinfo("click!", "i love clicks")


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="red")
frame.bind("<Button-1>", click)
frame.pack()

window.mainloop()
