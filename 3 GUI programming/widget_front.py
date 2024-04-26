import tkinter as tk


phase = "Quick brown fox jumps over the lazy dog"
window = tk.Tk()
label_1 = tk.Label(window, text=phase)
label_1.pack()
label_2 = tk.Label(window, text=phase, font=("Times", "12"))
label_2.pack()
label_3 = tk.Label(window, text=phase, font=("Arial", "16", "bold"))
label_3.pack()

window.mainloop()
