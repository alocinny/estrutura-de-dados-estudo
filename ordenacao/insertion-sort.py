def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        current_value = arr[i]
        j = i-1

        while j >= 0 and arr[j]>current_value:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = current_value

if __name__ == "__main__":
        lista = [64,34,25,12,22,11,90]
        print("lista original: ", lista)
        insertion_sort(lista)
        print("lista ordenada: ", lista)