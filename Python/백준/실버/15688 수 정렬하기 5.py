import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.nums = [int(input()) for _ in range(self.n)]

    def solve(self):
        self.nums.sort()

        for num in self.nums:
            print(num)


problem = Main()
problem.solve()