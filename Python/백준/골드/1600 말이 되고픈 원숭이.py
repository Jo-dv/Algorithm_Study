from collections import deque


class Main:
    def __init__(self):
        self.k = int(input())
        self.w, self.h = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.h)]
        self.horse_step = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
        self.monkey_step = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.visited = [[[False] * self.w for _ in range(self.h)] for _ in range(self.k + 1)]

    def is_valid(self, k, y, x):
        return 0 <= y < self.h and 0 <= x < self.w and not self.visited[k][y][x] and self.grid[y][x] != 1

    def bfs(self):
        dq = deque([(self.k, 0, 0, 0)])
        self.visited[self.k][0][0] = True

        while dq:
            k, y, x, step = dq.popleft()
            if y == self.h - 1 and x == self.w - 1:
                return step

            if k:  # 말의 움직임을 모두 수행한 후 원숭이의 움직임을 수행하는 것이 아님
                for s in self.horse_step:
                    my, mx = y + s[0], x + s[1]
                    if self.is_valid(k - 1, my, mx):
                        self.visited[k - 1][my][mx] = True
                        dq.append((k - 1, my, mx, step + 1))

            for s in self.monkey_step:
                my, mx = y + s[0], x + s[1]
                if self.is_valid(k, my, mx):
                    self.visited[k][my][mx] = True
                    dq.append((k, my, mx, step + 1))

        return -1

    def solve(self):
        print(self.bfs())


problem = Main()
problem.solve()
