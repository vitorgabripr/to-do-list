import tkinter as tk

class ComecarGrafica():
    def __init__(self):
        self.abrirJanela = tk.Tk()
        self.abrirJanela.title("Começando com Tkinter")

        caixaTexto = tk.Label(self.abrirJanela, text="Bem-vindo ao Tkinter!")
        caixaTexto.pack()

        self.abrirJanela.mainloop()

app = ComecarGrafica()
