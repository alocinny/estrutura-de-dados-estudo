#como eh uma lista duplamente encadeada, está faltando referencia para o nó anterior, então ela é somente encadeada

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class ListaDuplamentecircular:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head

        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node
    
    def remove(self, data):
        if self.head is None:
            return 'lista vazia'
        
        current = self.head
        while True:
            if current.data == data:
                if current == self.head:
                    if current.next == self.head:
                        self.head = None
                    else:
                        next_node = current.next
                        prev_node = current.prev
                        next_node.next = next_node
                        self.head = next_node
                
                else:
                    next_node = current.next
                    prev_node = current.prev
                    next_node.prev = prev_node
                    prev_node.next = next_node

            current = current.next
            if current == self.head:
                print(f"no com valor {data} nao encontrado")
                break
    
def main():
    t = ListaDuplamentecircular()
    t.insert(1)
    t.insert(3)
    t.insert(5)
    print(t.teste)

if __name__ == "__main__":
    main()