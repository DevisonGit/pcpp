import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application \nthat does nothing")


def are_you_sure():
    if messagebox.askyesno("", "Are you sure you want to quit the app?"):
        window.destroy()


def open_file():
    messagebox.showinfo("Open doc", "we'll open a file here")


def recent_file():
    for i in range(8):
        text = f"{i + 1}.file.txt"
        sub_sub_menu_file.add_command(label=text, underline=0)


window = tk.Tk()

main_menu = tk.Menu(window)
sub_menu_file = tk.Menu(main_menu, tearoff=0)
sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)

sub_menu_file.add_command(label="Open..", command=open_file, underline=0)
sub_menu_file.add_cascade(label="Open Recent file...", menu=sub_sub_menu_file, underline=5)
sub_menu_file.add_separator()
sub_menu_file.add_command(label="Quit", command=are_you_sure, underline=0)

recent_file()

main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
main_menu.add_command(label="About..", command=about_app, underline=1)

window.config(menu=main_menu)
window.mainloop()
