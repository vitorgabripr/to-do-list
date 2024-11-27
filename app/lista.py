class ListaToDo:
    
    def __init__(self):
        self.tarefas = []

    def adicionar_elemento(self, nome):
       if nome != '':
            self.tarefas.append(nome)
            return True
       return False
    def mostrar_tarefas(self):
        if not self.tarefas:
            return "Nenhuma tarefa adicionada ainda..."
        else:
           
            tarefas_texto = "\n".join(f"{i+1}. {tarefa}" 
                                      for i, tarefa in enumerate(self.tarefas))
            return tarefas_texto  

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
#programa = ListaToDo()
#programa.iniciar_programa()
