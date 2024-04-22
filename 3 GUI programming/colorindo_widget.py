import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1", bg="red", fg="yellow", activeforeground="green",
                     activebackground="green")
button_1.pack()

window.mainloop()
