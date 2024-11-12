from collections import deque


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.origin = [list(map(int, input().split())) for _ in range(self.m)]
        self.grid = [[0] * self.n for _ in range(self.m)]
        self.visited = [[False] * self.n for _ in range(self.m)]
        self.area = [-1]
        self.answer = [0, 0, 0]

    def search(self, y, x, num):
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 서북동남
        dq = deque([(y, x)])
        self.visited[y][x] = True
        self.grid[y][x] = num
        size = 1  # 방의 넓이

        while dq:
            current_y, current_x = dq.popleft()
            current_info = self.origin[current_y][current_x]  # 벽 정보
            for i in range(4):
                if current_info & (1 << i) == 0:
                    dy, dx = directions[i]
                    my, mx = current_y + dy, current_x + dx
                    if 0 <= my < self.m and 0 <= mx < self.n and not self.visited[my][mx]:
                        self.visited[my][mx] = True
                        self.grid[my][mx] = num
                        size += 1
                        dq.append((my, mx))

        self.area.append(size)  # 각 영역의 넓이
        self.answer[1] = max(self.answer[1], size)

    def find_max_area(self):
        for y in range(self.m):
            for x in range(self.n):
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    my, mx = y + dy, x + dx
                    if 0 <= my < self.m and 0 <= mx < self.n:
                        idx1, idx2 = self.grid[y][x], self.grid[my][mx]
                        if idx1 != idx2:  # 마주한 영역의 값이 다르면
                            self.answer[2] = max(self.answer[2], self.area[idx1] + self.area[idx2])  # 두 영역의 합

    def solve(self):
        num = 0
        for y in range(self.m):
            for x in range(self.n):
                if not self.visited[y][x]:
                    num += 1
                    self.answer[0] += 1
                    self.search(y, x, num)

        self.find_max_area()
        print(self.answer[0])
        print(self.answer[1])
        print(self.answer[2])


problem = Main()
problem.solve()
