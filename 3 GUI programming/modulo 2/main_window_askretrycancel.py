import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.askretrycancel("?", "Oops, i failed again!")
    print(answer)


window = tk.Tk()

button = tk.Button(window, text="What are your plans?", command=question)
button.pack()

window.mainloop()
