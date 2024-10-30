def selection_sort(arr):
    n = len(arr)
    temp = 0

    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j

        temp = arr[i] 
        arr[i] = arr[min_index]
        arr[min_index] = temp

if __name__ == "__main__":
        lista = [64,34,25,12,22,11,90]
        print("lista original: ", lista)
        selection_sort(lista)
        print("lista ordenada: ", lista)