from collections import deque


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.answer = 0

    def count_cheese(self):
        return sum(sum(i) for i in self.grid)

    def melt(self):
        dq = deque([(0, 0)])
        visited = [[False] * self.m for _ in range(self.n)]
        cheese = []  # 발견한 치즈를 저장

        while dq:
            y, x = dq.popleft()

            for dy, dx in self.directions:
                my = y + dy
                mx = x + dx
                if 0 <= my < self.n and 0 <= mx < self.m and not visited[my][mx]:
                    visited[my][mx] = True
                    if self.grid[my][mx] == 0:
                        dq.append((my, mx))
                    else:
                        cheese.append((my, mx))

        for y, x in cheese:  # 치즈를 발견하는 과정에서 바로 녹이면 빈 공간이 되면서 다른 치즈에 영향을 줌
            self.grid[y][x] = 0

        return len(cheese)  # 녹인 치즈의 수 반환

    def solve(self):
        rest_cheese = self.count_cheese()
        melted_cheese = 0

        while rest_cheese:
            melted_cheese = self.melt()
            rest_cheese -= melted_cheese
            self.answer += 1

        print(self.answer)
        print(melted_cheese)


problem = Main()
problem.solve()
