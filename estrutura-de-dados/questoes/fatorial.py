class Fatorial:

    def fatorial(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return Fatorial.fatorial(self, n-1)*n
    

def main():
    f = Fatorial()
    print(f.fatorial(6))

if __name__ == "__main__":
    main()

    #A recursão pode ser ineficiente em várias situações, especialmente se:

    #a) Subproblemas Repetidos
    #Em alguns algoritmos, como no Fibonacci recursivo, o mesmo subproblema é resolvido várias vezes, o que leva a uma redundância e aumento exponencial do número de chamadas recursivas.

    #Por exemplo, ao calcular fibonacci(5), o programa recalcula fibonacci(3) duas vezes e fibonacci(2) três vezes, resultando em uma ineficiência. Isso pode ser resolvido com memoização ou usando uma abordagem bottom-up (como a programação dinâmica).

    #b) Profundidade de Recursão Alta
    #Quando a profundidade da recursão é muito grande, há risco de estouro da pilha. Isso acontece porque, para cada chamada recursiva, uma nova entrada é adicionada à pilha de execução. Se houver chamadas demais, a pilha pode encher e o programa falhar.

    #Por exemplo, a recursão simples para calcular o fatorial pode funcionar bem para números pequenos, mas para valores muito grandes de n (como 10000), ela causará um estouro de pilha. Nesse caso, uma solução iterativa é mais eficiente.