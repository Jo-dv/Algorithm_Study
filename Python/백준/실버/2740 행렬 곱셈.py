class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.a = [list(map(int, input().split())) for _ in range(self.n)]
        self.m, self.k = map(int, input().split())
        self.b = [list(map(int, input().split())) for _ in range(self.m)]

    def solve(self):
        answer = []
        for i in zip(self.a):
            value = [sum([val1 * val2 for val1, val2 in zip(*i, j)]) for j in zip(*self.b)]
            answer.append(value)

        for i in answer:
            print(*i)


problem = Main()
problem.solve()
