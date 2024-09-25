class Item:
    def __init__(self, nome, categoria, subcategoria, prioridade=0):
        self.nome = nome
        self.categoria = categoria
        self.subcategoria = subcategoria
        self.prioridade = prioridade
        self.func_resp = None

    def def_prioridade(self, prioridade):
        self.prioridade = prioridade
    
    def atribuir_resp(self, funcionario):
        self.func_resp = funcionario

class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.itens_resp = []
    
    def add_item(self, item):
        self.itens_resp.append(item)
        self.atribuir_resp(self)

class Inventario:
    def __init__(self):
        self.inventario = []
    
    def push(self, item):
        self.inventario.append(item)

    def getSorted(self):
        return sorted(self.inventario, key = lambda item: item.prioridade, reversed = True)