import tkinter as tk

window = tk.Tk()

label_1 = tk.Label(window, height=10, text="arrow", cursor="arrow")
label_1.pack()
label_2 = tk.Label(window, height=10, text="clock", cursor="clock")
label_2.pack()
label_3 = tk.Label(window, height=10, text="heart", cursor="heart")
label_3.pack()

window.mainloop()
