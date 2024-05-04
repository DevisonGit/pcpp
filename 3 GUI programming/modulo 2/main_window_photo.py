import tkinter as tk

window = tk.Tk()
window.title("icon?")
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='logo.png'))
window.bind("<Button-1>", lambda e: window.destroy())
window.mainloop()
