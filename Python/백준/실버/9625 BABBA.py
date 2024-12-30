class Main:
    def __init__(self):
        self.k = int(input())

    def solve(self):
        a, b = 1, 0

        for _ in range(self.k):
            a, b = b, a + b

        print(a, b)


problem = Main()
problem.solve()