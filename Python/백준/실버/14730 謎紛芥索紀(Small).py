class Main:
    def __init__(self):
        self.n = int(input())
        self.terms = [list(map(int, input().split())) for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        for i in self.terms:
            c, k = i
            self.answer += (c * k)

        print(self.answer)


problem = Main()
problem.solve()