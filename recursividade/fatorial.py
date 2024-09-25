class Factorial:

    def __init__(self, num):
        self.num = num
    
    def fact(self):
        if self.num==1:
            return 1
        elif self.num==0:
            return 0
        else:
            return self.num * Factorial(self.num - 1).fact()
    
def main():
    f = Factorial(5)
    print(f.fact())

if __name__ == "__main__":
    main()