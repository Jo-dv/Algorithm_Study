from heapq import *
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.m, self.n = map(int, input().split())
        self.grid = [list(map(int, input())) for _ in range(self.n)]

    def search(self):
        costs = [[float('inf')] * self.m for _ in range(self.n)]
        hq = []
        heappush(hq, (0, 0, 0))
        costs[0][0] = 0

        while hq:
            cost, y, x = heappop(hq)
            if cost > costs[y][x]:
                continue

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                my = y + dy
                mx = x + dx
                if 0 <= my < self.n and 0 <= mx < self.m:
                    if cost + self.grid[my][mx] < costs[my][mx]:
                        costs[my][mx] = cost + self.grid[my][mx]
                        heappush(hq, (costs[my][mx], my, mx))

        print(costs[self.n - 1][self.m - 1])

    def solve(self):
        self.search()


problem = Main()
problem.solve()