#o tempo de execução cresce linearmente em relação ao tamanho de entrada. Cada elemento precisa ser processado uma vez

def find_max(arr):
    max_val = arr[0]

    for val in arr:
        if val > max_val:
            max_val = val
    return max_val

#neste caso, a função percorre cada elemento da lista uma vez para encontrar o mario valor. Portanto, ela tem uma complexidade de O9n), pois o tempo de execução aumenta linearmetne com o tamanho da lista