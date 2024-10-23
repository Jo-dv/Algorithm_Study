import sys
input = lambda: sys.stdin.readline().rstrip()

class Main:
    def __init__(self):
        self.n = int(input())
        self.records = [tuple(map(int, input().split())) for _ in range(self.n)]
        self.check = set()
        self.answer = 0

    def solve(self):
        for a, b in self.records:
            if b == 0:
                if a not in self.check:
                    self.answer += 1
                else:
                    self.check.remove(a)
            else:
                if a in self.check:
                    self.answer += 1
                else:
                    self.check.add(a)

        self.answer += len(self.check)
        print(self.answer)


problem = Main()
problem.solve()