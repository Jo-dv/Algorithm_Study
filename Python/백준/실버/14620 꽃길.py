class Main:
    def __init__(self):
        self.n = int(input())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.visited = [[False] * self.n for _ in range(self.n)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.answer = float('inf')

    def is_valid(self, y, x):  # 꽃의 겉잎 검사
        if self.visited[y - 1][x] == self.visited[y + 1][x] == self.visited[y][x - 1] == self.visited[y][x + 1] == False:
            return True

        return False

    def search(self, cost, seed):
        if seed == 3:
            self.answer = min(self.answer, cost)
            return

        for y in range(1, self.n - 1):
            for x in range(1, self.n - 1):
                if self.is_valid(y, x):
                    self.visited[y][x] = True
                    self.visited[y - 1][x] = True
                    self.visited[y + 1][x] = True
                    self.visited[y][x - 1] = True
                    self.visited[y][x + 1] = True
                    self.search(cost + self.grid[y][x] +
                                sum(self.grid[y + dy][x + dx] for dy, dx in self.directions), seed + 1)
                    self.visited[y][x] = False
                    self.visited[y - 1][x] = False
                    self.visited[y + 1][x] = False
                    self.visited[y][x - 1] = False
                    self.visited[y][x + 1] = False

    def solve(self):
        self.search(0, 0)
        print(self.answer)


problem = Main()
problem.solve()
