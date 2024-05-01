import tkinter as tk
from tkinter import messagebox


def clicked():
    messagebox.showinfo("info", "some\ninfo")


window = tk.Tk()
button_1 = tk.Button(window, text="Show info", command=clicked)
button_1.pack()
button_2 = tk.Button(window, text="Quit", command=window.destroy)
button_2.pack()

window.mainloop()
