import tkinter as tk


def next_lights():
    global counter
    phases_line = phases[counter]
    light_red = red if phases_line[0] is True else gray
    light_yellow = yellow if phases_line[1] is True else gray
    light_green = green if phases_line[2] is True else gray
    canvas.create_oval(80, 80, 20, 20, outline='black', width=2, fill=light_red)
    canvas.create_oval(80, 90, 20, 150, outline='black', width=2, fill=light_yellow)
    canvas.create_oval(80, 160, 20, 220, outline='black', width=2, fill=light_green)
    counter += 1
    if counter > 3:
        counter = 0


red = 'red'
gray = 'gray63'
yellow = 'yellow'
green = 'green'
phases = ((True, False, False),
          (True, True, False),
          (False, False, True),
          (False, True, False))

counter = 0
window = tk.Tk()
window.geometry("100x300")
window.resizable(width=False, height=False)
canvas = tk.Canvas(window, width=95, height=240, bg="gray25")
button = tk.Button(window, text="Quit", command=window.destroy)
button_next = tk.Button(window, text="Next", command=next_lights)
canvas.grid(row=1)
button_next.grid(row=2)
button.grid(row=3)
window.mainloop()
