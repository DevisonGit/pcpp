import random
import tkinter as tk
from tkinter import messagebox


def win(play):
    for i in range(3):
        if (tic_table[i][0].cget('text') == tic_table[i][1].cget('text') == tic_table[i][2].cget('text') == play or
                tic_table[0][i].cget('text') == tic_table[1][i].cget('text') == tic_table[2][i].cget('text') == play):
            return True
    if (tic_table[0][0].cget('text') == tic_table[1][1].cget('text') == tic_table[2][2].cget('text') == play or
            tic_table[0][2].cget('text') == tic_table[1][1].cget('text') == tic_table[2][0].cget('text') == play):
        return True
    return False


def circle(event):
    button = event.widget
    if button.cget('text') == '':
        button.config(text="O")
        if win("O"):
            messagebox.showinfo("", "You win")
            window.destroy()
        pc_play()


def pc_play():
    button_select = tic_table[random.randint(0, 2)][random.randint(0, 2)]
    if button_select.cget('text') == '':
        button_select.config(text="X")
        if win("X"):
            messagebox.showinfo("", "Pc player win")
            window.destroy()
    else:
        pc_play()


def create_table():
    for row in range(3):
        table = []
        for column in range(3):
            text = None
            if row == 1 and column == 1:
                text = "X"
            button = tk.Button(window, text=text, width=20, height=5)
            button.grid(row=row, column=column, sticky='nesw')
            button.bind("<Button-1>", circle)
            table.append(button)
        tic_table.append(table)


tic_table = []
window = tk.Tk()
window.title("TicTacToe")
create_table()
window.mainloop()
