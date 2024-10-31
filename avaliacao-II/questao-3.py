def sort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x< pivot]
    #middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x >= pivot]

    return sort(left) + [pivot] + sort(right)

#o código não está correto. Está faltando uma linha de código que seria para o pivot igual ao x, que quivaleria ao middle do array