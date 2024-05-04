import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.showwarning("Take care!", "Big brother is watching you!")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="What's going on?", command=question)
button.pack()
window.mainloop()
