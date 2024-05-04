import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='red')
button = tk.Button(window, text='Quit', command=window.destroy)

jpg = Image.open('logo_big.jpg')
image = ImageTk.PhotoImage(jpg)

canvas.create_image(200, 200, image=image)

canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
