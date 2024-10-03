class Main:
    def __init__(self):
        self.n = list(input())

    def solve(self):
        self.n.sort(reverse=True)
        num = "".join(i for i in self.n)
        num = int(num)
        print(num if num % 30 == 0 else -1)


problem = Main()
problem.solve()