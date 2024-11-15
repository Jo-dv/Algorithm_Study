from collections import deque


class Main:
    def __init__(self):
        self.r, self.c = map(int, input().split())
        self.grid = [list(input()) for _ in range(self.r)]

    def search_jihoon(self):
        for i in range(self.r):
            for j in range(self.c):
                if self.grid[i][j] == 'J':
                    self.grid[i][j] = '.'  # 위치를 공백으로 변경
                    return i, j

    def search_fires(self):
        fires = deque()
        for i in range(self.r):
            for j in range(self.c):
                if self.grid[i][j] == 'F':
                    fires.append((i, j, 0))  # 불의 위치와 시간 추가
        return fires

    def solve(self):
        y, x = self.search_jihoon()
        fires = self.search_fires()
        fire_time = [[1e10] * self.c for _ in range(self.r)]  # 불 확산 시간 테이블 초기화

        while fires:  # 불 확산
            fy, fx, ft = fires.popleft()
            if fire_time[fy][fx] <= ft:  # 이미 더 빠르게 도달한 경우 스킵(갱신된 경우)
                continue
            fire_time[fy][fx] = ft
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                my, mx = fy + dy, fx + dx
                if 0 <= my < self.r and 0 <= mx < self.c and self.grid[my][mx] == '.' and fire_time[my][mx] == 1e10:
                    fires.append((my, mx, ft + 1))

        dq = deque([(y, x, 0)])  # 지훈이 이동
        visited = [[False] * self.c for _ in range(self.r)]
        visited[y][x] = True

        while dq:
            y, x, t = dq.popleft()
            if y == 0 or y == self.r - 1 or x == 0 or x == self.c - 1:  # 가장자리에 도달한 경우 탈출 성공
                print(t + 1)  # 현재 시간 + 1이 탈출 시간
                return

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 이동 가능한 경우 탐색
                my, mx = y + dy, x + dx
                if 0 <= my < self.r and 0 <= mx < self.c and not visited[my][mx] and self.grid[my][mx] == '.':
                    if t + 1 < fire_time[my][mx]:  # 불보다 빨리 도달 가능한지 확인
                        visited[my][mx] = True
                        dq.append((my, mx, t + 1))

        print("IMPOSSIBLE")  # 탈출 불가한 경우


problem = Main()
problem.solve()