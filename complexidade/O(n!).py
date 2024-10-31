#o tempo de execução cresce fatorialmente, comum em algoritmos que geram todas as permutações possíveis de um conjunto

def generate_permutations(arr):
    if len(arr)==0:
        return [[]]
    permutations = []

    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for p in generate_permutations(rest):
            permutations.append([arr[i]]+p)
    
    return permutations

#essa função gera todas as permutações de uma lista, levando O(n!) operações, pois para cada elemento há (n-1)! permutações restantes

