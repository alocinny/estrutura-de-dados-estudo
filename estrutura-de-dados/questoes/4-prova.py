class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Tarefa:
    def __init__(self, descricao, responsavel, data_criacao):
        self.descricao = descricao
        self.responsavel = responsavel
        self.data_criacao = data_criacao
    
    def __str__(self):
        return f"Tarefa: {self.descricao}, Responsavel: {self.responsavel}, Data de criacao: {self.data_criacao}"
            

class PilhaTarefa:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def add_tarefa(self, tarefa):
        node = Node(tarefa)
        node.next = self.top
        self.top = node
        self.size += 1

    def visualizar(self):
        if self.top is None:
            return 'nenhuma tarefa foi adicionada'
        return self.top.data

def main():
    t1 = Tarefa("teste", "fulano 1", "1")
    t2 = Tarefa("teste2", "fulano 2", "2")
    t3 = Tarefa("teste3", "fulano 3", "3")

    p = PilhaTarefa()
    p.add_tarefa(t1)
    p.add_tarefa(t2)
    p.add_tarefa(t3)

    print(p.visualizar())

if __name__ == "__main__":
    main()