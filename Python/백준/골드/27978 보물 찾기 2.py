from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.h, self.w = map(int, input().split())
        self.grid = [list(input()) for _ in range(self.h)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def find_target(self):
        found = [None, None]
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x] == 'K':
                    found[0] = (y, x)
                if self.grid[y][x] == '*':
                    found[1] = (y, x)
                if None not in found:
                    return found

    def search(self, boat, treasure):
        costs = [[float('inf')] * self.w for _ in range(self.h)]
        by, bx = boat
        costs[by][bx] = 0
        dq = deque([(0, by, bx)])

        while dq:
            cost, y, x, = dq.popleft()
            if (y, x) == treasure:
                print(cost)
                return

            if costs[y][x] < cost:
                continue

            for dy, dx in self.directions:
                my = y + dy
                mx = x + dx
                if 0 <= my < self.h and 0 <= mx < self.w and self.grid[my][mx] != '#':
                    next_cost = float('inf')
                    if (my, mx) in [(y - 1, x + 1), (y, x + 1), (y + 1, x + 1)]:
                        next_cost = cost
                    else:
                        next_cost = cost + 1

                    if next_cost < costs[my][mx]:
                        if next_cost == cost:
                            dq.appendleft((next_cost, my, mx))
                        else:
                            dq.append((next_cost, my, mx))
                        costs[my][mx] = next_cost

        print(-1)

    def solve(self):
        boat, treasure = self.find_target()
        self.search(boat, treasure)


problem = Main()
problem.solve()