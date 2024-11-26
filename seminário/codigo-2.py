import networkx as nx
import matplotlib.pyplot as plt
import time

# Função para criar um grafo com dependências
def criar_grafo():
    G = nx.DiGraph()
    # Adicionando nós (representam instruções ou tarefas)
    G.add_nodes_from(["A", "B", "C", "D", "E"])
    # Adicionando arestas (representam dependências)
    G.add_edges_from([
        ("A", "B"),  # B depende de A
        ("A", "C"),  # C depende de A
        ("B", "D"),  # D depende de B
        ("C", "D"),  # D depende de C
        ("D", "E"),  # E depende de D
    ])
    return G

# Função para buscar hazards de dados, exibindo o grafo a cada iteração
def buscar_hazards_e_plotar(grafo):
    hazards = []
    pos = nx.spring_layout(grafo)  # Layout fixo para o grafo

    for node in grafo.nodes:
        predecessores = list(grafo.predecessors(node))
        
        # Exibir o grafo com destaque para o nó atual
        plotar_grafo_durante_analise(grafo, pos, node)

        # Verifica dependências que podem causar hazards
        if len(predecessores) > 1:
            for i in range(len(predecessores)):
                for j in range(i + 1, len(predecessores)):
                    # Verifica se dois predecessores têm um nó em comum como sucessor
                    pre1, pre2 = predecessores[i], predecessores[j]
                    if pre1 in grafo and pre2 in grafo:
                        hazards.append((pre1, pre2, node))
    return hazards

# Função para exibir o grafo durante a análise
def plotar_grafo_durante_analise(grafo, pos, no_atual):
    # Cor padrão para os nós
    node_colors = ['lightblue' if node != no_atual else 'yellow' for node in grafo.nodes]

    # Desenha o grafo
    plt.figure(figsize=(8, 6))
    nx.draw(
        grafo, pos, with_labels=True, 
        node_color=node_colors, edge_color='gray', 
        arrowsize=20, font_size=10
    )
    
    plt.title(f"Analisando nó: {no_atual}")
    plt.pause(3)  # Pausa para visualizar a análise

# Função para destacar hazards no grafo
def plotar_grafo_com_hazards(grafo, hazards):
    pos = nx.spring_layout(grafo)  # Define layout do grafo

    # Cor padrão para nós e arestas
    node_colors = ['lightblue'] * len(grafo.nodes)
    edge_colors = ['gray'] * len(grafo.edges)

    # Mapeia arestas para índices para fácil manipulação
    edge_list = list(grafo.edges)
    
    # Atualiza cores para arestas que fazem parte dos hazards
    for pre1, pre2, node in hazards:
        if (pre1, node) in edge_list:
            edge_colors[edge_list.index((pre1, node))] = 'red'
        if (pre2, node) in edge_list:
            edge_colors[edge_list.index((pre2, node))] = 'red'

    # Desenha o grafo
    plt.figure(figsize=(8, 6))
    nx.draw(
        grafo, pos, with_labels=True, 
        node_color=node_colors, edge_color=edge_colors, 
        arrowsize=20, font_size=10
    )
    
    # Adiciona rótulos às arestas
    nx.draw_networkx_edge_labels(
        grafo, pos, edge_labels={(u, v): f"{u}->{v}" for u, v in grafo.edges}
    )
    plt.title("Grafo com Hazards Destacados")
    plt.show()

# Exemplo de uso
grafo = criar_grafo()
hazards = buscar_hazards_e_plotar(grafo)

# Exibir hazards encontrados
if hazards:
    print("\nHazards encontrados:")
    for hazard in hazards:
        print(f"Hazard entre {hazard[0]} e {hazard[1]} no nó {hazard[2]}")
else:
    print("\nNenhum hazard encontrado.")

# Plotar o grafo destacando hazards
plotar_grafo_com_hazards(grafo, hazards)
