#Implemente uma Lista Encadeada de
#registros dos alunos. Cada registro
#deve conter a matrícula, nome e notas
#dos alunos.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Registro:

    def __init__(self, matricula, nome, notas):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas
    
    def __str__(self):
        return f"Matricula: {self.matricula}, Nome: {self.nome}, Notas: {self.notas}"
    
class Lista:
    def __init__(self):
        self.alunos = []
        self.head = None
    
    def push(self, dados):
        node = Node(dados)
        node.next = self.head
        self.head = node

        self.alunos.append(dados)
        self.next = node
        
