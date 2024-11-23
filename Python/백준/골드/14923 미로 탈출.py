from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.hy, self.hx = map(lambda i: int(i) - 1, input().split())
        self.ey, self.ex = map(lambda i: int(i) - 1, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.answer = float('inf')

    def search(self):
        dq = deque([])
        visited = [[[False] * self.m for _ in range(self.n)] for _ in range(2)]
        dq.append((self.hy, self.hx, 0, 1))
        visited[1][self.hy][self.hx] = True

        while dq:
            y, x, step, cnt = dq.popleft()
            if y == self.ey and x == self.ex:
                print(step)
                return

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                my, mx = y + dy, x + dx
                if 0 <= my < self.n and 0 <= mx < self.m and not visited[cnt][my][mx]:
                    if cnt == 1 and self.grid[my][mx] == 1:
                        dq.append((my, mx, step + 1, 0))
                        visited[0][my][mx] = True
                    if self.grid[my][mx] == 0:
                        dq.append((my, mx, step + 1, cnt))
                        visited[cnt][my][mx] = True

        print(-1)

    def solve(self):
        self.search()


problem = Main()
problem.solve()