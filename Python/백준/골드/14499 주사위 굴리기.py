from collections import deque


class Main:
    def __init__(self):
        self.n, self.m, self.y, self.x, self.k = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.commands = list(map(lambda x: int(x) - 1, input().split()))
        self.directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        self.col = deque([0, 0, 0, 0])
        self.row = deque([0, 0, 0, 0])

    def setup(self):
        if self.grid[self.y][self.x] == 0:
            self.grid[self.y][self.x] = self.col[1]
        else:
            self.col[1] = self.grid[self.y][self.x]
            self.row[1] = self.grid[self.y][self.x]
            self.grid[self.y][self.x] = 0

    def solve(self):
        for command in self.commands:
            dy, dx = self.directions[command]
            my = self.y + dy
            mx = self.x + dx
            if 0 <= my < self.n and 0 <= mx < self.m:
                self.y = my
                self.x = mx

                if command <= 1:
                    self.row.rotate(-1 if command == 0 else 1)
                    self.col[1] = self.row[1]
                    self.col[3] = self.row[3]
                    self.setup()
                else:
                    self.col.rotate(1 if command == 2 else -1)
                    self.row[1] = self.col[1]
                    self.row[3] = self.col[3]
                    self.setup()

                print(self.col[-1])


problem = Main()
problem.solve()