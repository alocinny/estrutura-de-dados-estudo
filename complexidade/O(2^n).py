#o tempo de execução cresce exponencialmente com o tamanho da entrada, típico de algoritmos que exploram todas as combinações possíveis, como cálculo de fibonacci sem memorização

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

#a função de fibonacci recursiva faz duas chamadas para cada valor de n, resultando em O(2^n) operações, pois o número de chamadas dobra a cada incremento de n