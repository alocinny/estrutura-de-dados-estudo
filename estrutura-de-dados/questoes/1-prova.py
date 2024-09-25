class Item:

    def __init__(self, nome, categoria, subacategoria):
        self.nome = nome
        self.categoria = categoria
        self.subcategoria = subacategoria
        self.prioridade = 0
        self.func_resp = None

    def definir_prioridade(self, prioridade):
        self.prioridade = prioridade

    def atribuir_resp(self, funcionario):
        self.func_resp = funcionario

    def __str__(self):
        return f"Item: {self.nome}, Categoria: {self.categoria}, Subcategoria {self.subcategoria}, Prioridade {self.prioridade}, Responsavel {self.func_resp.nome if self.func_resp else 'Nenhum'}"

class Funcionario:
    def __init__(self,nome):
        self.nome = nome
        self.itens_resp = []

    def adicionar_item_responsavel(self, item):
        self.itens_resp.append(item)
        item.atribuir_resp(self)
    
    def listar_itens_resp(self):
        return [str(item) for item in self.itens_resp]
    
    def __str__(self):
        return f"Funcionario: {self.nome}"

class Inventario:
    
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def listar_itens(self):
        return [str(item) for item in self.itens]
    
    def listar_itens_por_prioridade(self):
        return sorted(self.itens, key=lambda item: item.prioridade, reverse=True)
    
    def __str__(self):
        return "/n".join(self.listar_itens())