import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.k, self.l = map(int, input().split())
        self.wait = [input() for _ in range(self.l)]
        self.check = dict()

    def solve(self):
        for i in self.wait:
            if self.check.get(i):
                self.check.pop(i)
            self.check[i] = True

        result = []
        for i in self.check:
            result.append(i)
            if len(result) == self.k:
                break

        for i in result:
            print(i)


problem = Main()
problem.solve()
