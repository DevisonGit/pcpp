import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.place(x=10, y=10, w=150)
button_2.place(x=20, y=40)
button_3.place(x=30, y=70, h=50)

window.mainloop()
