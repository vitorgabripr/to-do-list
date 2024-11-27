import tkinter as tk
from lista import ListaToDo as ltd

listaTd = ltd


#comecando a parte grafica

#a classe ComecarGrafica é pra dar start no programa
class ComecarGrafica():
    def __init__(self):
        #cria a janela principal
        self.abrirJanela = tk.Tk()
        self.abrirJanela.title("2DO_List")

        self.abrirJanela.configure(bg="gray")

        #chama a funcao caixaEstrada
        self.caixaEntrada()
    

        self.abrirJanela.mainloop()#exibe a janela

#funcao a funcao q muda o estilo do programa
    def caixaEntrada(self):
        caixaTexto = tk.Label(
            self.abrirJanela,
            text="2DO_List",
            bg="gray",
            fg="white",
            font=("Arial", 16, "bold")
        )
        caixaTexto.pack()
    
#fucao para add tarefas
    def addTarefa(self):
        nome = self.lis

app = ComecarGrafica()
