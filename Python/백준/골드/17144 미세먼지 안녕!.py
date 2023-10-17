import copy


class Main:
    def __init__(self):
        self.r, self.c, self.t = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.r)]
        self.direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.answer = 2  # 공청기에 의해 빠지는 값을 미리 보충

    def solve(self):
        for _ in range(self.t):
            self.spread()
            self.clear()

        for i in self.grid:
            self.answer += sum(i)
        print(self.answer)

    def spread(self):
        temp = []
        for r in range(self.r):
            for c in range(self.c):
                if self.grid[r][c] > 0:
                    temp.append([r, c, self.grid[r][c]])  # 미리 먼지 값을 받아야 나중에 확산 값을 덮어쓰지 않고 올바르게 계산 가능

        for i in temp:
            y, x, dust = i
            cnt = 0
            for d in self.direction:
                my, mx = y + d[0], x + d[1]
                if 0 <= my < self.r and 0 <= mx < self.c and self.grid[my][mx] != -1:
                    self.grid[my][mx] += (dust // 5)
                    cnt += 1
            self.grid[y][x] -= (dust // 5) * cnt

    def clear(self):
        cleaner = []
        clear_grid = copy.deepcopy(self.grid)

        for r in range(self.r):
            for c in range(self.c):
                if self.grid[r][c] == -1:
                    cleaner.append([r, c])  # 먼저 들어오는 값이 상, 다음이 하

        r1, c1 = cleaner[0]  # 반시계 방향
        self.grid[r1][1] = 0  # 첫 값을 이동한 후에는 공청기에 의해 옮겨질 값이 없기 때문에 0으로 처리
        for i in range(2, self.c):
            self.grid[r1][i] = clear_grid[r1][i-1]
        for i in range(r1-1, -1, -1):
            self.grid[i][self.c-1] = clear_grid[i+1][self.c-1]
        for i in range(self.c-2, -1, -1):
            self.grid[0][i] = clear_grid[0][i+1]
        for i in range(1, r1):
            self.grid[i][0] = clear_grid[i-1][0]

        r2, c2 = cleaner[1]  # 시계 방향
        self.grid[r2][1] = 0
        for i in range(2, self.c):
            self.grid[r2][i] = clear_grid[r2][i-1]
        for i in range(r2+1, self.r):
            self.grid[i][self.c-1] = clear_grid[i-1][self.c-1]
        for i in range(self.c-2, -1, -1):
            self.grid[self.r-1][i] = clear_grid[self.r-1][i+1]
        for i in range(self.r-2, r2, -1):
            self.grid[i][0] = clear_grid[i+1][0]


problem = Main()
problem.solve()