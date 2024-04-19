import tkinter

# cria a janela principal
skylight = tkinter.Tk()

# da um titulo a janela
skylight.title("skylight")

# cria um botao
button = tkinter.Button(skylight, text="Bye")

# coordenadas do botao
button.place(x=10, y=10)

# inicia o controlador
skylight.mainloop()
