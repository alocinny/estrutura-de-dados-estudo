class Fibonacci:

    def __init__(self, num):
        self.num = num

    def fibo(self):
        if self.num == 0:
            return 0
        elif self.num == 1:
            return 1
        else: 
            return Fibonacci(self.num-1).fibo() + Fibonacci(self.num-2).fibo()

def main():
    f = Fibonacci(6)
    print(f.fibo())

if __name__ == "__main__":
    main()