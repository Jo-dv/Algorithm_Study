import heapq
from collections import deque


class Main:
    def __init__(self):
        self.n = int(input())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        self.shark_size = 2
        self.cnt = 0
        self.answer = 0

    def search_shark(self):
        for y in range(self.n):
            for x in range(self.n):
                if self.grid[y][x] == 9:
                    return y, x

    def check_validation(self, y, x, visited):  # 이동 유효성 검사
        return 0 <= y < self.n and 0 <= x < self.n and not visited[y][x] and self.grid[y][x] <= self.shark_size

    def grow(self):
        self.cnt += 1

        if self.cnt == self.shark_size:
            self.shark_size += 1
            self.cnt = 0

    def consume(self, init_y, init_x):
        visited = [[False] * self.n for _ in range(self.n)]
        visited[init_y][init_x] = True  # 위치가 이동될 때마다 재탐색을 수행해야 하므로
        dq = deque([(init_y, init_x, 0)])  # 현재 위치, 거리
        result = []

        while dq:
            y, x, distance = dq.popleft()

            for d in self.directions:
                my, mx = y + d[0], x + d[1]
                if self.check_validation(my, mx, visited):
                    dq.append((my, mx, distance + 1))
                    visited[my][mx] = True
                    if self.grid[my][mx] != 0 and self.grid[my][mx] < self.shark_size:  # 섭취할 먹이가 존재
                        heapq.heappush(result, (distance + 1, my, mx))  # 거리, 가장 위, 가장 왼쪽 순으로 고려

        return result

    def solve(self):
        y, x = self.search_shark()  # 초기 아기 상어 위치
        self.grid[y][x] = 0  # 아기 상어의 초기 위치를 0으로 초기화

        while True:
            shark = self.consume(y, x)  # 먹이 섭취
            if len(shark) == 0:  # 더 이상 섭취할 수 없다면, 엄마 상어에게 도움 요청
                break

            distance, my, mx = heapq.heappop(shark)  # 섭취 결과
            self.answer += distance
            self.grid[my][mx] = 0  # 이동 및 섭취 결과 반영
            y, x = my, mx
            self.grow()

        print(self.answer)


problem = Main()
problem.solve()
