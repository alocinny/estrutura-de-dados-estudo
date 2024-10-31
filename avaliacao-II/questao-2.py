def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        current_value = arr[i]
        j=i-1

        while j>= 0 and arr[j] > current_value:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = current_value

#na melhor das hipóteses o tempo vai ser ded complexidade O(n) pois caso o j não seja maior ou igual a 0 e o valor na posição j do array n seja maior que o current_value, a função vai percorrer os elementos do array de uma vez 
#na pior das hipóteses, vai ser preciso fazer dois loops aninhados, resultando em uma complexidade O(n^2)