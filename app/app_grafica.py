import tkinter as tk
from lista import ListaToDo  # Certifique-se de que o arquivo ListaToDo.py está no mesmo diretório

# Instanciar a classe ListaToDo
lista_to_do = ListaToDo()

# Função para adicionar item à lista
def add_item():
    item = entry.get()  # Obtém o texto da entrada
    if item:
        sucesso = lista_to_do.adicionar_elemento(item)  # Adiciona o item na lista do backend
        if sucesso:
            listbox.insert(tk.END, item)  # Adiciona o item na Listbox
            entry.delete(0, tk.END)  # Limpa a entrada de texto

# Configurando a janela principal
root = tk.Tk()
root.title("To-Do List")

# Label
label = tk.Label(root, text="Minha To-Do List")  # Configura o label
label.pack(pady=10)

# Entrada para novos itens
entry = tk.Entry(root, width=50)  # Criei a entrada de texto
entry.pack(pady=5)

# Botão para adicionar item
add_button = tk.Button(root, text="Adicionar", command=add_item)  # Adicionei o comando para chamar add_item
add_button.pack(pady=5)

# Lista de tarefas
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=20)

# Executar a aplicação Tkinter
root.mainloop()
