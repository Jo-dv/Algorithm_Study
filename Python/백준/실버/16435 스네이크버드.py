class Main:
    def __init__(self):
        self.n, self.l = map(int, input().split())
        self.h = list(map(int, input().split()))
        self.answer = self.l

    def solve(self):
        self.h.sort()
        for i in self.h:
            if self.answer >= i:
                self.answer += 1
            else:
                break

        print(self.answer)


problem = Main()
problem.solve()