from collections import deque


class Main:
    def __init__(self):
        self.h, self.w = map(int, input().split())
        self.grid = [list(input().strip()) for _ in range(self.h)]
        self.adjacent = None
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def mark_adjacent_walls(self):
        adjacent = [[-1] * self.w for _ in range(self.h)]
        # -1: 벽에 인접하지 않은 빈칸
        # 0: 벽에 인접한 빈칸
        # 1: 벽
        for i in range(self.h):
            for j in range(self.w):
                if self.grid[i][j] == '#':  # 벽
                    adjacent[i][j] = 1
                    continue
                for dy, dx in self.directions:
                    my, mx = i + dy, j + dx
                    if 0 <= my < self.h and 0 <= mx < self.w and self.grid[my][mx] == '#':
                        adjacent[i][j] = 0  # 벽에 인접한 빈칸
                        break

        return adjacent

    def find_points(self):
        start = end = None
        for i in range(self.h):
            for j in range(self.w):
                if self.grid[i][j] == "S":
                    start = (i, j)
                if self.grid[i][j] == "E":
                    end = (i, j)
                if start and end:
                    return start, end

    def search(self, start, end):
        dq = deque([])
        distance = [[float('inf')] * self.w for _ in range(self.h)]  # 시작점부터의 최단 거리 기록
        sy, sx = start
        distance[sy][sx] = 0
        dq.append((0, sy, sx))  # (이동 시간, y좌표, x좌표)

        while dq:
            time, y, x = dq.popleft()
            if (y, x) == end:
                print(time)
                return

            if distance[y][x] < time:
                continue

            for dy, dx in self.directions:
                my, mx = y + dy, x + dx
                if 0 <= my < self.h and 0 <= mx < self.w:
                    new_time = float('inf')
                    if self.adjacent[y][x] == 0 and self.adjacent[my][mx] == 0:  # 벽타기 -> 벽 위로 올라가는 거 아님
                        new_time = time
                    elif self.adjacent[my][mx] != 1:  # 벽으로는 이동할 수 없음
                        new_time = time + 1

                    if distance[my][mx] > new_time:  # 최소 시간 갱신
                        distance[my][mx] = new_time
                        if new_time == time:  # 비용이 0일 때는 앞에 추가
                            dq.appendleft((new_time, my, mx))
                        else:  # 비용이 1일 때는 뒤에 추가
                            dq.append((new_time, my, mx))

    def solve(self):
        start, end = self.find_points()
        self.adjacent = self.mark_adjacent_walls()  # 벽 인접 여부를 표시하는 2차원 배열
        self.search(start, end)


problem = Main()
problem.solve()