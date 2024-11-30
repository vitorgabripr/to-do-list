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
    
    import tkinter as tk

# Função para adicionar item à lista (isso chamaria uma função no seu backend)
def add_item():
    item = entry.get()
    if item:
        ltd.add_to_do(item)
        listbox.insert(tk.END, item)  # Insere o item na lista
        entry.delete(0, tk.END)

# Configurando a janela principal
root = tk.Tk()
root.title("2-Do List")

# Label
label = tk.Label(root, text="2DoList")
label.pack(pady=10)

# Entrada para novos itens
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Botão para adicionar item
add_button = tk.Button(root, text="Adicionar", command=add_item)
add_button.pack(pady=5)

# Lista de tarefas
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=20)

# Executar a aplicação Tkinter
root.mainloop()


#app = ComecarGrafica()
