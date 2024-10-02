import sys
input = lambda: sys.stdin.readline()


class Main:
    def __init__(self):
        self.n = int(input())
        self.nums = [int(input()) for _ in range(self.n)]

    def solve(self):
        self.nums.sort(reverse=True)
        for i in self.nums:
            print(i)


problem = Main()
problem.solve()