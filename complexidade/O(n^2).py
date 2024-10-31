#o tempo de execução cresce quadráticamente com o tamanho da entrada, comum em algoritmos de ordenação menos eficientes, como o bubble sort

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#o bubble sorte compara todos os pares adjacentes, o que resulta em uma complexidade O(n^2), pois há duas camadas de loop que dependem do tamanho da lista