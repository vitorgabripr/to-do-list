class ListaToDo:
    
    def __init__(self):
        self.tarefas = []

    def adicionar_elemento(self):
        nome = input("Digite o nome da tarefa: \n")
        self.tarefas.append(nome)
        print(f"Tarefa '{nome}' adicionada com sucesso!")
        
    def mostrar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa adicionada ainda.")
        else:
            print("Tarefas:")
            for i, tarefa in enumerate(self.tarefas):
                print(f"{i+1}. {tarefa}")

    def iniciar_programa(self):
        continuar = True
        while continuar:
            self.adicionar_elemento()  # Usa self para chamar os métodos da classe
            self.mostrar_tarefas()

            resposta = input("Deseja adicionar mais tarefas? (s/n): \n")
            if resposta.lower() != "s":
                continuar = False
                print("Fim do programa!")


# Inicializa a classe e chama o programa
programa = ListaToDo()
programa.iniciar_programa()
