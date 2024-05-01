import tkinter as tk

window = tk.Tk()

button_1 = tk.Button(window, text="Regular Button")
button_1["anchor"] = "e"
button_1["width"] = 20
button_1.pack()
button_2 = tk.Button(window, text="Another Button")
button_2["anchor"] = "sw"
button_2["width"] = 20
button_2["height"] = 3
button_2.pack()

window.mainloop()
