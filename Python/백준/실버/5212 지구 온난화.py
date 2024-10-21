class Main:
    def __init__(self):
        self.r, self.c = map(int, input().split())
        self.grid = [["."] * (self.c + 2)] + \
                    [["."] + list(input()) + ["."] for _ in range(self.r)] + \
                    [["."] * (self.c + 2)]

    def solve(self):
        island = [(y, x) for y in range(1, self.r + 1) for x in range(1, self.c + 1) if self.grid[y][x] == 'X']
        checked = [[False] * (self.c + 2) for _ in range(self.r + 2)]

        for y, x in island:
            cnt = 0
            checked[y][x] = True
            for dy, dx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if not checked[dy][dx] and self.grid[dy][dx] == ".":
                    cnt += 1
            if 3 <= cnt:
                self.grid[y][x] = "."

        rest_island = [(y, x) for y in range(1, self.r + 1) for x in range(1, self.c + 1) if self.grid[y][x] == "X"]
        lu_y = min(rest_island, key=lambda x: x[0])[0]
        lu_x = min(rest_island, key=lambda x: x[1])[1]
        rd_y = max(rest_island, key=lambda x: x[0])[0]
        rd_x = max(rest_island, key=lambda x: x[1])[1]

        for y in range(min(lu_y, rd_y), max(lu_y, rd_y) + 1):
            for x in range(min(lu_x, rd_x), max(lu_x, rd_x) + 1):
                print(self.grid[y][x], end='')
            print()


problem = Main()
problem.solve()