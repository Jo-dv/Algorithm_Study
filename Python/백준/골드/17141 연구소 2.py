from collections import deque


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.answer = float('inf')

    def check_virus(self):
        return [(i, j) for i in range(self.n) for j in range(self.n) if self.grid[i][j] == 2]

    def select_virus(self, virus):  # 바이러스 조합 탐색
        result = []

        def select(idx, selected):
            if len(selected) == self.m:
                result.append(selected)
                return
            if idx == len(virus):
                return
            select(idx + 1, selected + [virus[idx]])
            select(idx + 1, selected)

        select(0, [])
        return result

    def search(self, selected_virus):
        result = 0
        for viruses in selected_virus:
            visited = [[False if self.grid[i][j] != 1 else True for j in range(self.n)] for i in range(self.n)]
            check = [[-1 if self.grid[i][j] != 1 else 1 for j in range(self.n)] for i in range(self.n)]
            dq = deque([])
            max_time = 0
            for virus in viruses:
                y, x = virus
                visited[y][x] = True
                check[y][x] = 0
                dq.append((y, x, 0))

            while dq:
                y, x, time = dq.popleft()
                max_time = max(max_time, time)  # 가장 오래 걸리는 시간
                for dy, dx in self.directions:
                    my, mx = y + dy, x + dx
                    if 0 <= my < self.n and 0 <= mx < self.n and not visited[my][mx]:
                        dq.append((my, mx, time + 1))
                        visited[my][mx] = True
                        check[my][mx] = time + 1

            if sum(i.count(-1) for i in check) == 0:  # 빈 공간이 없을 때만 정답 갱신
                self.answer = min(self.answer, max_time)  # 가장 오래 걸리는 시간 중 최단 시간
            else:
                result += 1

        if result == len(selected_virus):  # 모든 경우를 다 뒤졌음에도 바이러스를 모두 퍼뜨릴 수 없다면
            print(-1)
        else:
            print(self.answer)

    def solve(self):
        virus = self.check_virus()
        selected_virus = self.select_virus(virus)
        self.search(selected_virus)


problem = Main()
problem.solve()
