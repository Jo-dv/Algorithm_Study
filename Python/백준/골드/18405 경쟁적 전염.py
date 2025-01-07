import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.s, self.x, self.y = map(int, input().split())
        self.visited = [[False] * self.n for _ in range(self.n)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def init_virus(self):
        viruses = {i: [] for i in range(1, self.k + 1)}

        for i in range(self.n):
            for j in range(self.n):
                virus = self.grid[i][j]
                if virus in viruses:
                    viruses[virus].append((i, j))
                    self.visited[i][j] = True

        return viruses

    def spread(self, viruses):
        for _ in range(self.s):
            for virus in range(1, self.k + 1):
                new_virus = []
                for y, x in viruses[virus]:
                    for dy, dx in self.directions:
                        my = y + dy
                        mx = x + dx
                        if 0 <= my < self.n and 0 <= mx < self.n and not self.visited[my][mx]:
                            self.visited[my][mx] = True
                            self.grid[my][mx] = virus
                            new_virus.append((my, mx))

                    viruses[virus] = new_virus

    def solve(self):
        viruses = self.init_virus()
        self.spread(viruses)

        print(self.grid[self.x - 1][self.y - 1])


problem = Main()
problem.solve()
