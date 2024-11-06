class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.a = list(map(int, input().split()))
        self.b = list(map(int, input().split()))

    def solve(self):
        self.a.extend(self.b)
        self.a.sort()
        print(*self.a)


problem = Main()
problem.solve()