import networkx as nx
import matplotlib.pyplot as plt

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
        predecessores = list(grafo.predecessors(node))
        print("lista predecessores ", predecessores, "\n")
        # Verifica dependências que podem causar hazards
        if len(predecessores) > 1:
            print("entrou no if > 1 ", predecessores, "\n")
            for i in range(len(predecessores)):
                for j in range(i + 1, len(predecessores)):
                    print("entrou no for ", predecessores[i], " ", predecessores[j], "\n")
                    # Verifica se dois predecessores têm um nó em comum como sucessor
                    pre1, pre2 = predecessores[i], predecessores[j]
                    if pre1 in grafo and pre2 in grafo:
                        print("entrou no if pre1 e pre2 ", pre1, " ", pre2, "\n")
                        hazards.append((pre1, pre2, node))
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

# Plotar o grafo
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, with_labels=True, node_color='lightblue', edge_color='gray')
nx.draw_networkx_edge_labels(grafo, pos, edge_labels={(u, v): f"{u}->{v}" for u, v in grafo.edges})
plt.show()