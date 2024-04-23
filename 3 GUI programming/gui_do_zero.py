import tkinter as tk

window = tk.Tk()

# label widget não clicavel apresenta um pequeno texto
label = tk.Label(window, text="Little label")
label.pack()

# frame widget não clicavel usado para agrupar widgets e separalos visualmente
frame = tk.Frame(window, height=30, width=100, bg="blue")
frame.pack()

# botão
button = tk.Button(window, text="Button")
button.pack(fill=tk.X)

# componente invisivel
switch = tk.IntVar()
switch.set(1)

# checkbutton representa seleções de dois estados
checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
checkbutton.pack()

# Entry permite inserção de dados simples
entry = tk.Entry(window, width=30)
entry.pack()

# radio button circulos preenchidos com um ponto ou não
radiobutton_1 = tk.Radiobutton(window, text="beef", variable=switch, value=0)
radiobutton_2 = tk.Radiobutton(window, text="salad", variable=switch, value=1)
radiobutton_1.pack()
radiobutton_2.pack()

window.mainloop()
