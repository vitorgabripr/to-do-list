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
