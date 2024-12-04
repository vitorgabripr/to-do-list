import tkinter as tk
from tkinter import ttk

# Função para adicionar tarefa
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        tk.messagebox.showwarning("Aviso", "Por favor, insira uma tarefa.")

# Configuração da janela principal
root = tk.Tk()
root.title("To-Do List")

# Configuração do estilo
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10))
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TListbox", font=("Helvetica", 12))

#tema

style.theme_use_fonts = True
style.theme_use("clam")


# Criação dos widgets
frame_top = tk.Frame(root)
frame_top.pack(pady=10)
frame_top.configure(bg="#f0f0f0")


entrada_tarefa = ttk.Entry(frame_top, width=35)
entrada_tarefa.pack(side=tk.LEFT, padx=5)
entrada_tarefa.configure(style="TEntry", font="Helvetica", background="#ffffff")


botao_adicionar = ttk.Button(frame_top, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(side=tk.LEFT)

lista_tarefas = tk.Listbox(root, width=50, height=10, font=("Helvetica", 12))
lista_tarefas.pack(pady=10)

# Loop principal
root.mainloop()
