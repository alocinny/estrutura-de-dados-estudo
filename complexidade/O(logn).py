# o tempo de execução cresce logaritmicamente em relaçõa ao tamanho da entrada, comum em algoritmos de busca binária.

def binary_search(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else: 
            right = mid -1
    return -1

#a busca binária divide a lista ao meio a cada iteração, resultando em O(log n) operações, pois o número de comparações cresce logaritmicamente com o tamanho da lista

