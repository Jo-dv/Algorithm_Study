from collections import deque


class Main:
    def __init__(self):
        self.n, self.k, self.m = map(int, input().split())
        self.dq = deque([])
        self.result = []
        self.flag = True

    def solve(self):
        for i in range(1, self.n + 1):
            self.dq.append(i)

        while self.dq:
            if self.result and len(self.result) % self.m == 0:
                self.flag = not self.flag
            self.dq.rotate(-self.k if self.flag else self.k - 1)
            self.result.append(self.dq.pop())

        for i in self.result:
            print(i)


problem = Main()
problem.solve()