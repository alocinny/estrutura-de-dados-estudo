class Fibonacci:

    def __init__(self, num):
        self.num = num

    def fibo(self, depth=0):
        indent = "  " * depth  # Cria a indentação com base na profundidade da recursão
        print(f"{indent}Calculando Fibonacci({self.num})")  # Exibe a chamada com a indentação correspondente

        if self.num == 0:
            print(f"{indent}Fibonacci({self.num}) = 0")  # Mostra o resultado para o caso base 0
            return 0
        elif self.num == 1:
            print(f"{indent}Fibonacci({self.num}) = 1")  # Mostra o resultado para o caso base 1
            return 1
        else:
            # Realiza as chamadas recursivas com nível de profundidade incrementado
            left = Fibonacci(self.num - 1).fibo(depth + 1)
            right = Fibonacci(self.num - 2).fibo(depth + 1)
            result = left + right
            print(f"{indent}Fibonacci({self.num}) = {left} + {right} = {result}")  # Exibe as somas e o resultado
            return result

def main():
    f = Fibonacci(8)  # Altere para o valor desejado
    print(f"Resultado final: {f.fibo()}")

if __name__ == "__main__":
    main()
