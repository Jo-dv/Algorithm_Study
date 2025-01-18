class Main:
    def __init__(self):
        self.a, self.b, self.n = map(int, input().split())

    def solve(self):
        result = 0
        for _ in range(self.n):
            self.a = (self.a % self.b) * 10
            result = self.a // self.b

        print(result)


problem = Main()
problem.solve()