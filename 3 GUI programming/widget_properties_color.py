import tkinter as tk

window = tk.Tk()

button_1 = tk.Button(window, text="Ordinary Button")
button_1.pack()
button_2 = tk.Button(window, text="Colorful Button")
button_2.pack()
button_2.config(bg="black", fg="yellow", activebackground="green", activeforeground="red")

window.mainloop()
