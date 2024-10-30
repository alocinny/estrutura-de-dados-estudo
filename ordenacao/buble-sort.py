#compara dois elementos, se o da esquerda for maior, troca de lugar e avança uma posição. Repete até ordenar. Complexidade O(n^2)

def bubble_sort(arr):
    
    n = len(arr) #comprimento do array
    temp = 0
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = temp
                    swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    lista = [64,34,25,12,22,11,90]
    print("lista original: ", lista)
    bubble_sort(lista)
    print("lista ordenada: ", lista)
