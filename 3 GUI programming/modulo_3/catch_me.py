import tkinter as tk
import random
from tkinter import messagebox


def you_won():
    messagebox.showinfo("Congrats", "You won")


def new_position(event):
    new_x = random.randint(10, 430)
    new_y = random.randint(10, 470)
    button.place(x=new_x, y=new_y)


window = tk.Tk()
window.title("Catch me!")
window.resizable(height=False, width=False)
window.geometry("500x500")

button = tk.Button(window, text="Catch me!", command=you_won)
button.place(x=10, y=10)
button.bind("<Enter>", new_position)

window.mainloop()
