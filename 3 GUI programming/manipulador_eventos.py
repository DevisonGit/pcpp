import tkinter


# metodo simples para manipular eventos
def click():
    skylight.destroy()


skylight = tkinter.Tk()
skylight.title("Skylight")

button = tkinter.Button(skylight, text='Bye', command=click)  # sera invocado quando o botão for clicado
button.place(x=10, y=10)

skylight.mainloop()
