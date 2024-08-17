import math
from collections import deque
from itertools import combinations as comb


class Virus:
    def __init__(self, y, x, time):
        self.y = y
        self.x = x
        self.time = time


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.answer = math.inf

    def search_virus(self):
        return [(i, j) for j in range(self.n) for i in range(self.n) if self.grid[i][j] == 2]

    def init_visited(self):
        visited = [[False] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 1:  # 벽은 모두 방문 처리
                    visited[i][j] = True

        return visited

    def check_result(self, visited):
        for i in range(self.n):
            for j in range(self.n):
                if not visited[i][j] and self.grid[i][j] == 0:  # 방문 안 한 곳 중에 길이 남아있다면
                    return False

        return True

    def bfs(self, pos):
        visited = self.init_visited()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dq = deque([Virus(y, x, 0) for y, x in pos])
        for y, x in pos:
            visited[y][x] = True
        final_time = 0

        while dq:
            current_virus = dq.popleft()

            for d in directions:
                my, mx = current_virus.y + d[0], current_virus.x + d[1]

                if 0 <= my < self.n and 0 <= mx < self.n and not visited[my][mx]:
                    visited[my][mx] = True
                    dq.append(Virus(my, mx, current_virus.time + 1))
                    if self.grid[my][mx] == 0:  # 비활성 바이러스는 통과할 수는 있으나
                        final_time = max(final_time, current_virus.time + 1)  # 감염 대상이 아니므로 감염 시간은 포함하지 않음

        return final_time if self.check_result(visited) else math.inf

    def select_virus(self, pos):
        return comb(pos, self.m)

    def solve(self):
        virus_pos = self.search_virus()  # 바이러스 위치 탐색
        selected_virus = self.select_virus(virus_pos)  # m개의 바이러스 선택
        for i in selected_virus:  # 선택된 바이러스 조합을 기준으로
            self.answer = min(self.answer, self.bfs(i))

        print(self.answer if self.answer != math.inf else -1)


problem = Main()
problem.solve()