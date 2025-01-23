

class Main:
    def __init__(self):
        self.n = int(input())
        self.a = list(map(int, input().split()))
        self.answer = []

    def solve(self):
        p = sorted(self.a)
        for i in self.a:
            temp = p.index(i)
            self.answer.append(temp)
            p[temp] = 0

        print(*self.answer)


problem = Main()
problem.solve()