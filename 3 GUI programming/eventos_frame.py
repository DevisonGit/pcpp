import tkinter as tk
from tkinter import messagebox


def click():
    tk.messagebox.showinfo("Click!", "I love clicks")


window = tk.Tk()

label = tk.Label(window, text="Label")
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="green")
frame.pack()

window.mainloop()
