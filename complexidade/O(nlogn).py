#comum em algoritmos de ordenação eficientes, como merge sort e heapsort

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left,right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

#o merge sort divide a listas repetidamente e então combina de forma ordenada, levando O(n*logn) operações. A divisão da lista é logarítmica, enquanto a combinação de elementos leva tempo linear
