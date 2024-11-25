import networkx as nx

# Função para criar um grafo com dependências
def criar_grafo():
    G = nx.DiGraph()
    # Adicionando nós (representam instruções ou tarefas)
    G.add_nodes_from(["A", "B", "C", "D", "E"])
    # Adicionando arestas (representam dependências)
    # A -> B: B depende de A
    G.add_edges_from([
        ("A", "B"),  # B depende de A
        ("A", "C"),  # C depende de A
        ("B", "D"),  # D depende de B
        ("C", "D"),  # D depende de C
        ("D", "E"),  # E depende de D
    ])
    return G

# Função para buscar hazards de dados
def buscar_hazards(grafo):
    hazards = []
    for node in grafo.nodes:
        # Para cada nó, verificamos os predecessores e sucessores
        predecessores = list(grafo.predecessors(node))
        sucessores = list(grafo.successors(node))
        # Hazard ocorre quando dois predecessores têm conflitos com o mesmo sucessor
        for i in range(len(predecessores)):
            for j in range(i + 1, len(predecessores)):
                if predecessores[i] in grafo and predecessores[j] in grafo:
                    if any(suc in grafo.successors(predecessores[i]) for suc in sucessores):
                        hazards.append((predecessores[i], predecessores[j], node))
    return hazards

# Exemplo de uso
grafo = criar_grafo()
hazards = buscar_hazards(grafo)

# Visualizar o grafo e os hazards encontrados
print("Grafo:")
for edge in grafo.edges:
    print(edge)

if hazards:
    print("\nHazards encontrados:")
    for hazard in hazards:
        print(f"Hazard entre {hazard[0]} e {hazard[1]} no nó {hazard[2]}")
else:
    print("\nNenhum hazard encontrado.")


import matplotlib.pyplot as plt

# Plotar o grafo
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, with_labels=True, node_color='lightblue', edge_color='gray')
nx.draw_networkx_edge_labels(grafo, pos, edge_labels={(u, v): f"{u}->{v}" for u, v in grafo.edges})
plt.show()